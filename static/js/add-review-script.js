$(document).ready(function(){
    // Initialise the book picker autocomplete and populate it with data from the books collection
    var bookNames = {};
    var bookNamesArray = $("#book-names li").text().split(".");
    bookNamesArray.pop();
    bookNamesArray.forEach(function(book){
        bookNames[book] = null;
    });
    $("input.autocomplete").autocomplete({
        data: bookNames,
        minLength: 0,
    });

    // Script to add functionality to the star picker
    $(".star-rating label").click(function(){
        $(this).children().addClass("amber-text");
        $(this).prevAll("label").children().addClass("amber-text");
        $(this).nextAll("label").children().removeClass("amber-text");
    })
});