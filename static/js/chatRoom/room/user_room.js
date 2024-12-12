"use strict";
const patientInfo = document.getElementById("warn");

// 从 data-* 属性中获取数据
const room = patientInfo.dataset.room;

var socket;

function main() {
    socket = new WebSocket(`ws://127.0.0.1:8000/room/number/${room}/`);

    socket.onopen = function () {
        console.log("WebSocket connection opened");
        socket.send("<|come in|>");
    };

    socket.onmessage = function (event) {
        var messageContainer = document.getElementById("message-container");
        var messageElement = document.createElement("div");
        var data = JSON.parse(event.data);
        messageElement.className = "message received";
        if (data.status === 'true') {
            if (data.message.startsWith("data:image")) {
                var img = document.createElement("img");
                img.src = data.message;
                messageElement.appendChild(img);
            } else {
                var fileInfo = data.message.split("file_url:");
                if (fileInfo[1] === undefined) {
                    messageElement.innerText = fileInfo[0];
                } else {
                    var link = document.createElement("a");
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

    document.getElementById("send-button").addEventListener("click", function () {
        var messageInput = document.getElementById("message-input");
        var fileInput = document.getElementById("file-input");
        var message = messageInput.value;
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
            var file = fileInput.files[0];
            if (file) {
                var reader = new FileReader();
                reader.onload = function (e) {
                    var dataURL = e.target.result;
                    if (dataURL.startsWith("data:image")) {
                        socket.send(dataURL);
                        var messageContainer = document.getElementById("message-container");
                        var messageElement = document.createElement("div");
                        messageElement.className = "message sent";
                        var img = document.createElement("img");
                        img.src = dataURL;
                        messageElement.appendChild(img);
                        messageContainer.appendChild(messageElement);
                        messageContainer.scrollTop = messageContainer.scrollHeight;
                        fileInput.value = "";
                    } else {
                        var formData = new FormData();
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
    var video = document.getElementById("video");
    var canvas = document.getElementById("canvas");
    var videoContainer = document.getElementById("video-container");
    var cameraButton = document.getElementById("camera-button");
    var takePhotoButton = document.getElementById("take-photo-button");

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
        var context = canvas.getContext("2d");
        context.drawImage(video, 0, 0, canvas.width, canvas.height);
        var dataURL = canvas.toDataURL("image/png");
        socket.send(dataURL);

        var messageContainer = document.getElementById("message-container");
        var messageElement = document.createElement("div");
        messageElement.className = "message sent";
        var img = document.createElement("img");
        img.src = dataURL;
        messageElement.appendChild(img);
        messageContainer.appendChild(messageElement);
        messageContainer.scrollTop = messageContainer.scrollHeight;

        videoContainer.style.display = "none";
        var stream = video.srcObject;
        var tracks = stream.getTracks();
        tracks.forEach(function (track) {
            track.stop();
        });
        video.srcObject = null;
    });
});

window.onbeforeunload = function (e) {
    return '确定离开此页吗？';
}