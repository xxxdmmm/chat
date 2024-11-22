"use strict";
let socket;

function createCard(data) {
    let card = document.createElement('div');
    card.className = 'card';
    card.style.marginBottom = '20px';

    let cardBody = document.createElement('div');
    cardBody.className = 'card-body';

    let cardTitle = document.createElement('h5');
    cardTitle.className = 'card-title';
    cardTitle.textContent = "患者姓名: " + data.name;

    let cardButton = document.createElement('button');
    if (data.ok === 0) {
        cardButton.className = 'btn btn-primary';
        cardButton.textContent = "分配医生";
    } else {
        cardButton.textContent = "已分配";
        cardButton.className = "btn btn-success";
        cardButton.disabled = true;
    }
    cardButton.name = data.patient_id;
    cardButton.id = data.name;
    cardButton.setAttribute('first', data.first);

    cardButton.addEventListener('click', function () {
        let modal = new bootstrap.Modal(document.getElementById('exampleModal'));
        document.getElementById('exampleModalLabel').textContent = "患者姓名: " + this.id;
        modal.show();
    });

    cardBody.appendChild(cardTitle);
    cardBody.appendChild(cardButton);
    card.appendChild(cardBody);
    document.getElementById('card-container').appendChild(card);
}

function main() {
    socket = new WebSocket("ws://127.0.0.1:8000/mange-list/");
    let receivedMessages = new Set();

    socket.onmessage = function (event) {
        let data = JSON.parse(event.data);
        let messageKey = data.patient_id;
        let patient_name = data.name;
        if (receivedMessages.has(messageKey)) {
            console.log("消息已存在，不生成新的卡片");
            let target = document.getElementById(patient_name);
            target.className = 'btn alert-danger';
            target.textContent = '对方请求重新分配医生';
            target.disabled = false;
            target.setAttribute('first', data.first);
            return;
        }
        createCard(data);
        receivedMessages.add(messageKey);
    };

    socket.onclose = function () {
        console.log("WebSocket连接已关闭");
        main();
    };
}

$(function () {
    main();
});


$(document).ready(function () {
    $('#confirm').click(function () {
        let selectedElement = $('.list-group-item.active');
        let selectedId = selectedElement.attr('id');
        let doctorName = selectedElement.text(); // 获取医生名字

        if (selectedId) {
            let patientName = $('#exampleModalLabel').text().split(': ')[1];
            let btn = $('#' + patientName)
            let patientId = btn.attr('name'); // 获取患者ID
            let first = btn.attr('first'); // 是否首次
            // 创建 WebSocket 连接
            let websocket_add = "ws://127.0.0.1:8000/doctor/message-list/" + selectedId + '/'
            let socket2 = new WebSocket(websocket_add);

            socket2.onopen = function () {
                console.log("WebSocket2连接已打开");
                // 发送数据
                let data = {
                    status: 'true',
                    doctor_id: selectedId,
                    patient_name: patientName,
                    patient_id: patientId, // 添加患者ID
                    first: first
                };
                socket2.send(JSON.stringify(data));
                console.log("数据已发送:", data);
            };

            socket2.onmessage = function (event) {
                let response = JSON.parse(event.data);
                console.log("收到服务器消息:", response);

                if (response.status === 'success') {
                    // 更新卡片内容
                    let cardButton = document.getElementById(patientName);
                    let cardTitle = cardButton.previousSibling;
                    cardTitle.textContent = "患者姓名: " + patientName + " - 已分配: " + doctorName; // 使用医生名字
                    cardButton.textContent = "已分配";
                    cardButton.className = "btn btn-success";
                    cardButton.disabled = true;
                    let proof = {
                        doctor_id: selectedId,
                        patient_id: patientId,
                        admin_send: "#$admin_send_for_user$#"
                    }
                    socket.send(JSON.stringify(proof));
                } else {
                    alert("分配失败," + doctorName.toString() + "医生未在线");
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
        }
    });

    $('.list-group-item').click(function () {
        $('.list-group-item').removeClass('active');
        $(this).addClass('active');
    });
});