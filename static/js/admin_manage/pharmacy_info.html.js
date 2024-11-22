$(document).ready(function () {
    $("#request-new").click(function () {
        location.reload();
    });
});

// 获取按钮
let backToTopButton = document.getElementById("back-to-top");

// 当用户滚动到一定距离时显示按钮
window.onscroll = function () {
    if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200) {
        backToTopButton.style.display = "block";
    } else {
        backToTopButton.style.display = "none";
    }
};

// 当用户点击按钮时，滚动到页面顶部
backToTopButton.onclick = function () {
    window.scrollTo({top: 0, behavior: 'smooth'});
};