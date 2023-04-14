$(".slide_nav").hide();

var isNavVisible = false;

$(".xi-bars").click(function () {
    if (isNavVisible) {
        $(".slide_nav").hide()
        $('.base').css("pointer-events", "auto");
        $('.base').removeClass('blur');
    } else {
        $(".slide_nav").fadeIn(500)
        $('.base').addClass('blur');
        $('.base').css("pointer-events", "none");
    }
    isNavVisible = !isNavVisible;
});

$('.nav-link').click(function () {
    $('.middle').addClass("change_background_color")
});