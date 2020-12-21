$(document).ready(function() {
    // The script here was adapted from this jsfiddle: http://jsfiddle.net/SirusDoma/ayf832td/
    $("#password").on("focusout", function () {
        if ($(this).val() != $("#passwordConfirm").val()) {
            $("#passwordConfirm").removeClass("valid").addClass("invalid");
        } else {
            $("#passwordConfirm").removeClass("invalid").addClass("valid");
        }
    });

    $("#confirm-password").on("keyup", function () {
        if ($("#password").val() != $(this).val()) {
            $(this).removeClass("valid").addClass("invalid");
        } else {
            $(this).removeClass("invalid").addClass("valid");
        }
    });
});