let socket2;

// 获取元素
const patientInfo = document.getElementById("patient_side_info");

// 从 data-* 属性中获取数据
const patientName = patientInfo.dataset.patientName;
const patientId = patientInfo.dataset.patientId;
const room = patientInfo.dataset.room;


function pharmacy_connect() {
    socket2 = new WebSocket("ws://127.0.0.1:8000/pharmacy/");
    socket2.onopen = function () {
        console.log("WebSocket2连接已打开");
    };

    socket2.onmessage = function (event) {
        let response = JSON.parse(event.data);
        console.log(response);
        if (response.room === room) {
            alert("药房已收到处方信息");
        }
    };

    socket2.onclose = function () {
        console.log("WebSocket2连接已关闭");
        pharmacy_connect();
    };
}

$(function () {
    $('#send_to_pharmacy').click(function () {
        let data;
        $.ajax({
            url: '/info/',
            type: 'POST',
            dataType: 'json',
            success: function (response) {
                data = response.data;
                $.ajax({
                    url: '/get_result/',
                    type: 'POST',
                    data: {
                        'patient_id': patientId
                    },
                    success: function (response) {
                        console.log("执行了2")
                        let _data = JSON.parse(response)
                        console.log(_data);
                        _data.patient_name = patientName;
                        _data.doctor_name = data.username;
                        console.log(_data.doctor_name)
                        _data.room = room;
                        socket2.send(JSON.stringify(_data));
                    },
                    error: function (xhr) {
                        alert("传输失败！");
                    }
                });
            }
        });

    })
})

$(function () {
    pharmacy_connect();
})
window.onbeforeunload = function (e) {
    return '确定离开此页吗？';
}