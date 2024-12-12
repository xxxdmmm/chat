"use strict";

function main() {
    let data;
    $.ajax({
        url: '/info/',
        type: 'POST',
        dataType: 'json',
        success: function (response) {
            data = response.data;

            let websocket_add = `ws://127.0.0.1:8000/user/message-list/${data.id}/`;
            let socket2 = new WebSocket(websocket_add);
            let receivedMessages = new Set();

            socket2.onopen = function () {
                console.log("WebSocket2连接已打开");
            };

            socket2.onmessage = function (event) {
                let data = JSON.parse(event.data);
                if (data.status === 'false') {
                    return;
                }
                let proof = $('#proof').attr("doctor_id");
                if (proof === data.doctor_id) {
                    $('#warn').text("已为您分配到医生，尽快进入聊天室，如果分配多个医生，请以最后一个为准");
                    $("#request-new").removeAttr("hidden").show();

                    function md5Encrypt(message) {
                        let hash = CryptoJS.MD5(message);
                        return hash.toString(CryptoJS.enc.Hex);
                    }


                    let messageKey = data.patient_id + data.doctor_name + data.doctor_id;

                    let message = "doctor_id:" + data.doctor_id + "+" + "user_id:" + data.patient_id;
                    let encode_room = md5Encrypt(message);

                    let response_data = {
                        status: 'success',
                        roomNum: encode_room
                    }
                    socket2.send(JSON.stringify(response_data));

                    // 检查消息是否已经存在
                    if (receivedMessages.has(messageKey)) {
                        console.log("消息已存在，不生成新的卡片");
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
                    cardTitle.textContent = "医生姓名: " + data.doctor_name;

                    let cardLink = document.createElement('a');
                    cardLink.className = 'card-link';
                    cardLink.href = "/doctor/" + encode_room.toString() + "/";
                    cardLink.textContent = "开始问诊";
                    cardLink.target = "_blank"

                    // 组装卡片元素
                    cardBody.appendChild(cardTitle);
                    cardBody.appendChild(cardLink);
                    card.appendChild(cardBody);

                    // 将卡片插入到页面中
                    document.getElementById('card-container').appendChild(card);
                } else {
                    let response_data = {
                        status: 'false',
                    }
                    socket2.send(JSON.stringify(response_data));
                }

            };

            socket2.onclose = function () {
                console.log("WebSocket连接已关闭");
                main();
            };
        }
    });


}

$(function () {
    main();
})