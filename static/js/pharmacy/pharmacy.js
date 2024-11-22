var socket;

function main() {
    socket = new WebSocket("ws://127.0.0.1:8000/pharmacy/");

    socket.onopen = function () {
        console.log("WebSocket连接已打开");
    };

    socket.onmessage = function (event) {
        console.log("收到请求")
        let data = JSON.parse(event.data);
        let response = {
            room: data.room
        }
        socket.send(JSON.stringify(response));

        $.ajax({
            url: '/get_form_check_and_crawl/',
            type: 'POST',
            success: function (formResponse) {
                let formData = JSON.parse(formResponse);
                // 删除已存在的行
                let existingRow = document.getElementById(`${'field_' + data.patient_id}`);
                let isReplacement = false;
                if (existingRow) {
                    existingRow.remove();
                    isReplacement = true;
                }

                // 动态生成新的表格行
                var newRow = `
                            <tr id="${'field_' + data.patient_id}">
                                <td id="${'field_' + data.patient_id + 'patient_name'}">${data.patient_name}</td>
                                <td id="${'field_' + data.patient_id + 'doctor_name'}">${data.doctor_name}</td>
                                <td id="${'field_' + data.patient_id + 'prescription'}" class="td-for-prescription">${data.prescription}</td>
                                <td id="${'field_' + data.patient_id + 'crawl_name_field'}">${formData.crawl_name_field}</td>
                                <td id="${'field_' + data.patient_id + 'check_name_field'}">${formData.check_name_field}</td>
                                <td>
                                    <input type="file" hidden="hidden" id="file_${data.patient_id}" accept="image/*">
                                    <button class='btn btn-primary' id="btn_${data.patient_id}">选择图片</button>
                                </td>
                                <td>
                                    <button class='btn btn-primary' id="save_${data.patient_id}">保存</button>
                                </td>
                                <td>${isReplacement ? "替换者" : ""}</td> <!-- 新增备注单元格 -->
                            </tr>
                        `;
                $('#data-table tbody').prepend(newRow);

                // 绑定选择图片按钮事件
                $(`#btn_${data.patient_id}`).click(function () {
                    $(`#file_${data.patient_id}`).click();
                });

                // 绑定保存按钮事件
                $(`#save_${data.patient_id}`).click(function () {
                    var prescription = data.prescription;
                    var symptom = data.symptom;
                    var patientName = $(`#${'field_' + data.patient_id + 'patient_name'}`).text();
                    var doctorName = $(`#${'field_' + data.patient_id + 'doctor_name'}`).text();
                    var crawlSelect = $(`#${'field_' + data.patient_id + 'crawl_name_field'} select`);
                    var crawlName = crawlSelect.val();
                    var checkSelect = $(`#${'field_' + data.patient_id + 'check_name_field'} select`);
                    var checkName = checkSelect.val();
                    var fileInput = $(`#file_${data.patient_id}`)[0];
                    var file = fileInput.files[0];

                    if (!crawlName || !checkName) {
                        alert("抓药人和监管确认不能为空！");
                        return;
                    }

                    if (!file) {
                        alert("请上传图片！");
                        return;
                    }

                    if (!file.type.startsWith('image/')) {
                        alert("上传的文件必须是图片！");
                        return;
                    }

                    // 构造FormData对象
                    var formData = new FormData();
                    formData.append('prescription', prescription);
                    formData.append('symptom', symptom);
                    formData.append('doctor_name', doctorName);
                    formData.append('patient_name', patientName);
                    formData.append('crawl_name', crawlName);
                    formData.append('check_name', checkName);
                    formData.append('image', file);
                    formData.append('patient_id', data.patient_id);

                    // 发送数据到后端
                    $.ajax({
                        url: '/upload_pharmacy_info/',
                        type: 'POST',
                        data: formData,
                        processData: false,
                        contentType: false,
                        success: function (response) {
                            alert("数据保存成功！");
                            // 修改保存按钮的状态和样式
                            var saveButton = $(`#save_${data.patient_id}`);
                            saveButton.text("已处理");
                            saveButton.prop("disabled", true);
                            saveButton.removeClass("btn-primary").addClass("btn-success");

                            // 禁用选择图片按钮
                            var chooseButton = $(`#btn_${data.patient_id}`);
                            chooseButton.prop("disabled", true);
                        },
                        error: function (xhr) {
                            alert("内部错误，保存失败！");
                        }
                    });
                });
            },
            error: function (xhr) {
                alert("内部错误!");
            }
        });
    };

    socket.onclose = function () {
        console.log("WebSocket连接已关闭");
        main();
    };
}

$(function () {
    main();
});

window.onbeforeunload = function (e) {
    return '确定离开此页吗？';
}