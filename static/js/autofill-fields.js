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

                    // Set the title, imgURL, description and ISBN variables
                    let title = book["title"];
                    let imgURL = book["imageLinks"]["thumbnail"];
                    let description = book["description"];
                    let ISBN = ""
                    for (var i = 0; i < book["industryIdentifiers"].length; i++) {
                        if (book["industryIdentifiers"][i]["type"] == "ISBN_10") {
                            ISBN = book["industryIdentifiers"][i]["identifier"];
                        }
                    }
                    
                    // Find the purchase link from the ISBN10
                    let purchaseLink = "https://www.amazon.com/dp/" + ISBN;

                    // Fill the book_name, img_url, purchase_link and description fields in the form
                    $("#book_name").val(title);
                    $("#img_url").val(imgURL);
                    $("#purchase_link").val(purchaseLink);
                    $("#description").val(description);

                }

            });

        }

    })

});