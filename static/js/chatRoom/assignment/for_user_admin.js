function request() {
    let data;
    $.ajax({
        url: '/info/',
        type: 'POST',
        dataType: 'json',
        success: function (response) {
            data = response.data;

            let name = data.username;
            let patient_id = data.id;
            let first = data.first
            let socket = new WebSocket("ws://127.0.0.1:8000/mange-list/");
            let message = {
                "patient_id": patient_id,
                "name": name,
                "first": first,
                'ok': 0
            }
            socket.onopen = function () {
                console.log("WebSocket连接已打开");
                socket.send(JSON.stringify(message));
            };

            socket.onmessage = function (event) {
                let data = JSON.parse(event.data);
                let text = document.getElementById("warn").textContent;
                if (text === "已为您分配到医生，尽快进入聊天室，如果分配多个医生，请以最后一个为准") {
                    message.ok = 1;
                }
                if (data.admin_send === "#$admin_send_for_detect$#") {
                    socket.send(JSON.stringify(message));
                }
                if (data.admin_send === "#$admin_send_for_user$#" && data.patient_id === patient_id) {
                    let target = $('#proof');
                    target.attr('doctor_id', data.doctor_id);
                }
            };

            socket.onclose = function () {
                console.log("WebSocket连接已关闭");
                request();
            };
        }
    });


}

$(function () {
    request();
});

$(document).ready(function () {
    // 添加点击事件处理程序
    $("#request-new").click(function () {
        location.reload();
    });
});

window.onbeforeunload = function (e) {
    return '确定离开此页吗？';
}