$(document).ready(function(){

    function AutofillFromGoogleBooks(autofillFrom, bookName, author, ISBN) {
        /*
        function that searches the google books API for book data from either book name
        and author or ISBN and inputs the data into the form.
        :autofillFrom: string that specifies whether to autofill from book name and author or ISBN.
        :bookName: string that gives the bookName
        :author: string that gives the bookName
        :ISBN: string that gives the ISBN
        */

        // store the id of the warning text p in a variable warningText
        let warningID = "";
        let warningMessage = "";

        // build the query that will be used to search google books API
        let query = "https://www.googleapis.com/books/v1/volumes?q=";
        if (autofillFrom == "Name+Author") {

            query += "intitle:" + bookName + "+inauthor:" + author;
            warningID = "#autofill-warning";
            warningMessage = "Check the book name and author are correct!";

        } else if (autofillFrom == "ISBN") {

            query += "isbn:" + ISBN;
            warningID = "#autofill-ISBN-warning";
            warningMessage = "Check the ISBN10 is correct!";

        }

        // Now query google books API with the query
        $.get(query, function(response) {

            // Warn the user if there is no data for the book they input
            if (!response["items"]) {
                
                $(warningID).text("No data found! " + warningMessage);

            } else {

                // Store the data for the first book from the response in a variable
                let book = response["items"][0]["volumeInfo"];

                // Set the title, imgURL, description and ISBN variables
                let title = book["title"];
                let authors = "";
                for (var i = 0; i < book["authors"]["length"]; i++) {

                    if (i > 0) authors += ", ";
                    authors += book["authors"][i];

                }
                let imgURL = book["imageLinks"]["thumbnail"];
                let description = book["description"];
                let ISBN = ""
                for (var i = 0; i < book["industryIdentifiers"].length; i++) {
                    if (book["industryIdentifiers"][i]["type"] == "ISBN_10") ISBN = book["industryIdentifiers"][i]["identifier"];
                }
                
                // Find the purchase link from the ISBN10
                let purchaseLink = "https://www.amazon.com/dp/" + ISBN;

                // Fill the book_name, img_url, purchase_link and description fields in the form
                $("#book_name").val(title);
                $("#author").val(authors);
                $("#img_url").val(imgURL);
                $("#purchase_link").val(purchaseLink);
                $("#description").val(description);
                $("#ISBN").val(ISBN);           
            }
        });
    }

    $("#autofill-fields").click(function() {

        // Reset the autofill warning text
        $("#autofill-warning").text("");
        $("#autofill-ISBN-warning").text("");

        // Get the book's name and author from the form
        let bookName = $("#book_name").val();
        let author = $("#author").val();

        // Check if the book's name and author are filled in
        if (bookName == "" || author == "") {

            $("#autofill-warning").text("You must fill in the book name and author first!");

        } else {

            AutofillFromGoogleBooks("Name+Author", bookName, author, "");

        }

    });

    $("#autofill-ISBN").click(function() {

        // Reset the autofill warning text
        $("#autofill-ISBN-warning").text("");
        $("#autofill-warning").text("");

        // Get the book's name and author from the form
        let ISBN = $("#ISBN").val();

        // Check if the book's name and author are filled in
        if (ISBN == "") {

            $("#autofill-warning").text("You must fill in the ISBN first!");

        } else {

            AutofillFromGoogleBooks("ISBN", "", "", ISBN);

        }

    });

});