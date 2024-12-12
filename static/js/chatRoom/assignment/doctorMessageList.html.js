"use strict";

function main() {
    let data;
    $.ajax({
        url: '/info/',
        type: 'POST',
        dataType: 'json',
        success: function (response) {
            data = response.data;

            let websocket_add = `ws://127.0.0.1:8000/doctor/message-list/${data.id}`;
            let socket = new WebSocket(websocket_add);
            let receivedMessages = new Set();
            let doctor_name = data.username;

            socket.onopen = function () {
                console.log("WebSocket连接已打开");
            };

            socket.onmessage = function (event) {
                let data = JSON.parse(event.data);

                if (data.status === 'true') {

                    //应答admin
                    let response_data = {
                        status: 'success'
                    }
                    socket.send(JSON.stringify(response_data));

                    console.log(event.data);

                    let messageKey = data.patient_id + data.patient_name + data.doctor_id;
                    let patient_id = data.patient_id;

                    let first = data.first;
                    console.log(first);
                    // 检查消息是否已经存在
                    if (receivedMessages.has(messageKey)) {
                        console.log("消息已存在，不生成新的卡片");
                        let target = document.getElementById(patient_id);
                        target.className = 'btn btn-warning';
                        target.href = "#";
                        target.target = "";
                        target.textContent = "重新应答请求";
                        return;
                    }

                    // 记录新消息
                    receivedMessages.add(messageKey);

                    // 创建卡片元素
                    let card = document.createElement('div');
                    card.className = 'card';
                    card.style.marginBottom = '20px';

                    let cardBody = document.createElement('div');
                    cardBody.className = 'card-body';

                    let cardTitle = document.createElement('h5');
                    cardTitle.className = 'card-title';
                    cardTitle.textContent = "患者姓名: " + data.patient_name;


                    let cardLink = document.createElement('a');
                    cardLink.id = data.patient_id;
                    cardLink.className = 'btn btn-primary';
                    cardLink.href = "#";
                    cardLink.textContent = "接受问诊请求";
                    cardLink.setAttribute('patient_id', data.patient_id);
                    cardLink.setAttribute('doctor_id', data.doctor_id);
                    cardLink.setAttribute('doctor_name', doctor_name);

                    cardLink.addEventListener('click', function () {
                        let patient_id = this.getAttribute("patient_id");
                        let doctor_id = this.getAttribute("doctor_id");
                        let doctor_name = this.getAttribute("doctor_name");
                        let cardLinkLink = this;
                        // 创建 WebSocket 连接
                        let websocket_add = "ws://127.0.0.1:8000/user/message-list/" + patient_id + "/";
                        let socket2 = new WebSocket(websocket_add);

                        socket2.onopen = function () {
                            console.log("WebSocket2连接已打开");

                            // 发送数据
                            var data = {
                                doctor_id: doctor_id,
                                doctor_name: doctor_name,
                                patient_id: patient_id, // 添加患者ID
                                name: "doctor"
                            };
                            socket2.send(JSON.stringify(data));
                            console.log("数据已发送:", data);
                        };

                        socket2.onmessage = function (event) {
                            var response = JSON.parse(event.data);
                            console.log("收到服务器消息:", response);
                            console.log(first);
                            if (response.status === 'success') {
                                cardLinkLink.textContent = "进入问诊室";
                                cardLinkLink.target = "_blank";
                                cardLink.className = 'btn btn-success';
                                cardLinkLink.href = "/room/forDoctor/" + response.roomNum.toString() + "/?patient_id=" + patient_id.toString() +
                                    "&patient_name=" + data.patient_name.toString() + "&first=" + first.toString();

                                console.log(cardLinkLink.href)
                            } else {
                                cardLinkLink.textContent = "对方已下线，消息过期";
                                cardLinkLink.href = "#";
                                cardLinkLink.className = "btn btn-danger";
                                cardLinkLink.target = "";
                                cardLinkLink.disabled = true;
                            }
                            // 无论成功或失败，都关闭 WebSocket 连接
                            socket2.close();
                        };

                        socket2.onerror = function (error) {
                            console.log("WebSocket2错误:", error);
                            socket2.close();  // 在发生错误时关闭连接
                        };

                        socket2.onclose = function () {
                            console.log("WebSocket2连接已关闭");
                        };
                    });


                    // 组装卡片元素
                    cardBody.appendChild(cardTitle);
                    cardBody.appendChild(cardLink);
                    card.appendChild(cardBody);

                    // 将卡片插入到页面中
                    document.getElementById('card-container').appendChild(card);
                }
            };

            socket.onclose = function () {
                console.log("WebSocket连接已关闭");
                main();
            };
        }
    });
}

$(function () {
    main();
})

window.onbeforeunload = function (e) {
    return '确定离开此页吗？';
}