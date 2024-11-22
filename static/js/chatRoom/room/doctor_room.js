var socket;

function main() {
    const url = new URL(window.location.href);
    // 使用 URLSearchParams 获取查询参数
    const roomNum = url.pathname.split('/')[3];  // 解析 roomNum

    socket = new WebSocket(`ws://127.0.0.1:8000/room/number/${roomNum}/`);
    socket.onopen = function () {
        console.log("WebSocket1 connection opened");
        socket.send("<|come in|>");
    };

    socket.onmessage = function (event) {
        let messageContainer = document.getElementById("message-container");
        let messageElement = document.createElement("div");
        let data = JSON.parse(event.data);
        messageElement.className = "message received";
        if (data.status === 'true') {
            if (data.message.startsWith("data:image")) {
                let img = document.createElement("img");
                img.src = data.message;
                messageElement.appendChild(img);
            } else {
                let fileInfo = data.message.split("file_url:");
                if (fileInfo[1] === undefined) {
                    messageElement.innerText = fileInfo[0];
                } else {
                    let link = document.createElement("a");
                    link.href = fileInfo[1];
                    console.log(fileInfo[1]);
                    link.textContent = fileInfo[0];
                    link.target = "_blank";
                    messageElement.appendChild(link);
                }
            }

            messageContainer.appendChild(messageElement);
            messageContainer.scrollTop = messageContainer.scrollHeight;
        } else if (data.status === 'false') {
            alert("对方还未进入/已退出该房间，暂时无法接受您的消息");
        } else if (data.status === 'other-in') {
            alert("对方已经进入房间！");
        } else if (data.status === 'other-out') {
            alert("对方已经退出房间！");
        } else {
            alert("内部错误，请联系管理员!")
        }

    };

    socket.onclose = function () {
        console.log("WebSocket connection closed");
        main();
    };

    $("#send-button").click(function () {
        let messageInput = document.getElementById("message-input");
        let fileInput = document.getElementById("file-input");
        let message = messageInput.value;
        if (message.trim()) {
            socket.send(message);
            var messageContainer = document.getElementById("message-container");
            var messageElement = document.createElement("div");
            messageElement.className = "message sent";
            messageElement.innerText = message;
            messageContainer.appendChild(messageElement);
            messageContainer.scrollTop = messageContainer.scrollHeight;
            messageInput.value = "";
        } else {
            messageInput.value = "";
        }

        if (fileInput.files.length > 0) {
            let file = fileInput.files[0];
            if (file) {
                let reader = new FileReader();
                reader.onload = function (e) {
                    var dataURL = e.target.result;
                    if (dataURL.startsWith("data:image")) {
                        socket.send(dataURL);
                        let messageContainer = document.getElementById("message-container");
                        let messageElement = document.createElement("div");
                        messageElement.className = "message sent";
                        let img = document.createElement("img");
                        img.src = dataURL;
                        messageElement.appendChild(img);
                        messageContainer.appendChild(messageElement);
                        messageContainer.scrollTop = messageContainer.scrollHeight;
                        fileInput.value = "";
                    } else {
                        let formData = new FormData();
                        formData.append('file', file);

                        $.ajax({
                            url: '/upload/',
                            type: 'POST',
                            data: formData,
                            processData: false,
                            contentType: false,
                            success: function (response) {
                                var fileURL = response.file_url;
                                socket.send(file.name + "file_url:" + fileURL);
                                var messageContainer = document.getElementById("message-container");
                                var messageElement = document.createElement("div");
                                messageElement.className = "message sent";
                                var link = document.createElement("a");
                                link.href = fileURL;
                                link.textContent = file.name;
                                link.target = "_blank";
                                messageElement.appendChild(link);
                                messageContainer.appendChild(messageElement);
                                messageContainer.scrollTop = messageContainer.scrollHeight;
                            }
                        });
                        fileInput.value = "";
                    }
                };
                reader.readAsDataURL(file);
            }
        }
    });
}


$(function () {
    main();
    // 摄像头功能
    let video = document.getElementById("video");
    let canvas = document.getElementById("canvas");
    let videoContainer = document.getElementById("video-container");
    let cameraButton = document.getElementById("camera-button");
    let takePhotoButton = document.getElementById("take-photo-button");

    cameraButton.addEventListener("click", function () {
        navigator.mediaDevices.getUserMedia({video: true}).then(function (stream) {
            video.srcObject = stream;
            videoContainer.style.display = "flex";
        }).catch(function (err) {
            console.log("发生错误: " + err);
        });
    });

    takePhotoButton.addEventListener("click", function () {
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        let context = canvas.getContext("2d");
        context.drawImage(video, 0, 0, canvas.width, canvas.height);
        let dataURL = canvas.toDataURL("image/png");
        socket.send(dataURL);

        let messageContainer = document.getElementById("message-container");
        let messageElement = document.createElement("div");
        messageElement.className = "message sent";
        let img = document.createElement("img");
        img.src = dataURL;
        messageElement.appendChild(img);
        messageContainer.appendChild(messageElement);
        messageContainer.scrollTop = messageContainer.scrollHeight;

        videoContainer.style.display = "none";
        let stream = video.srcObject;
        let tracks = stream.getTracks();
        tracks.forEach(function (track) {
            track.stop();
        });
        video.srcObject = null;
    });
})

