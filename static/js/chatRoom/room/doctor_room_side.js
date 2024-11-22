// 获取元素
const patientInfo = document.getElementById("patient_side_info");

// 从 data-* 属性中获取数据
const patientName = patientInfo.dataset.patientName;
const patientId = patientInfo.dataset.patientId;
const first = patientInfo.dataset.first;
const room = patientInfo.dataset.room;


if (first === 'True') {
    $("#some_warn").removeAttr("hidden").show();
} else {
    $("#btn-group").removeAttr("hidden").show();
}


function get_side() {
    var container = $('#side');
    $.ajax({
        url: '/room/sideDoctor/get/', // 修改为处理请求的URL
        type: 'POST',
        data: {
            'patient_id': patientId
        },
        success: function (response) {
            container.html(response);
            binding();
        }
        ,
        error: function (xhr) {
            container.html('<p>无法加载数据，请稍后重试。</p>');
        }
    })
    ;
}

function binding() {
    // 使用 Ajax 在打开模态框时加载内容

    $('.disease-link').on('click', function (e) {
        e.preventDefault();
        var name = $(this).data('name');
        $('#dynamicModalLabel').text(name);
        var modalBody = $('#dynamicModalBody-form');

        $.ajax({
            url: `/get/patient/${patientId}/info/`, // 修改为处理请求的URL
            type: 'GET',
            data: {
                'field': name
            },
            success: function (response) {
                modalBody.html(response);
            },
            error: function (xhr) {
                modalBody.html('<p>无法加载数据，请稍后重试。</p>');
            }
        });
    });
}


$(function () {
    get_side();
})

$(function () {
    // 拦截表单提交事件
    $('#dynamicModalBody-form').on('submit', function (e) {
        e.preventDefault();  // 阻止默认表单提交

        // 获取表单数据
        var formData = $(this).serialize();

        // 发送AJAX请求
        $.ajax({
            type: 'POST',
            url: $(this).attr('action'),
            data: formData,
            success: function (response) {
                let data = JSON.parse(response);
                if (data.field === '选择跟踪项目') {
                    $("#some_warn").hide().attr("hidden", "hidden");
                    $("#btn-group").removeAttr("hidden").show();
                    get_side();
                }
                alert('数据已成功更新！');
            },
            error: function (xhr, status, error) {
                // 处理错误
                alert('数据更新失败，请稍后再试。');
            }
        });
    });
})

$(function () {
    $('#renew').click(function () {
        renew();
    })
})

function renew() {
    $.ajax({
        url: '/renew/table/',
        type: 'POST',
        data: {
            'patient_id': patientId
        },
        success: function (response) {
            alert("操作成功!");
            get_side();
            $("#some_warn").removeAttr("hidden").show();
            $("#btn-group").hide().attr("hidden", "hidden");
            $('#create_new_table').prop('disabled', false);
        }
        ,
        error: function (xhr) {
            alert("操作失败!");
        }
    });
}

$(function () {
    $('#create_new_table').click(function () {
        $.ajax({
            url: '/room/table/create/',
            type: 'POST',
            data: {
                'patient_id': patientId
            },
            success: function (response) {
                alert("创建成功!");
                $('#create_new_table').prop('disabled', true);
            },
            error: function (xhr) {
                alert("创建失败！");
            }
        });
    })
})

$(function () {
    $('#get_table_btn').click(function () {
        get_table();
    })
})

function get_table() {
    $.ajax({
        url: '/get/patient/table/',
        type: 'POST',
        data: {
            'patient_id': patientId
        },
        success: function (response) {
            $('#patient_table').html(response);
        },
        error: function (xhr) {
            alert("获取好转表失败");
        }
    });
}

$(function () {
    $('#get_choose').click(function () {
        get_choose();
    })
})

function get_choose() {
    $.ajax({
        url: '/get/patient/choose/',
        type: 'POST',
        data: {
            'patient_id': patientId
        },
        success: function (response) {
            $('#patient_table2').html(response);
        },
        error: function (xhr) {
            alert("获取选择表失败");
        }
    });
}