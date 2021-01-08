$(document).ready(function(){

    $("#autofill-fields").click(function() {

        // Reset the autofill warning text
        $("#autofill-warning").text("");

        // Get the book's name and author from the form
        let bookName = $("#book_name").val();
        let author = $("#author").val();

        // Check if the book's name and author are filled in
        if (bookName == "" || author == "") {

            $("#autofill-warning").text("You must fill in the book name and author first!");

        } else {

            // Query the google books API for the data
            $.get("https://www.googleapis.com/books/v1/volumes?q=intitle:" + bookName + "+inauthor:" + author, function(response) {

                // Warn the user if there is no data for the book they input
                if (!response["items"]) {
                    
                    $("#autofill-warning").text("No data found! Check the book name and author are correct!");

                } else {

                    // Store the data for the first book from the response in a variable
                    let book = response["items"][0]["volumeInfo"];
                    console.log(book);

                    // Set the imgURL and description
                    let imgURL = book["imageLinks"]["thumbnail"];
                    let description = book["description"];

                    // Fill the imgURL and description fields in the form
                    $("#img_url").val(imgURL);
                    $("#description").val(description);

                }

            });

        }

    })

});