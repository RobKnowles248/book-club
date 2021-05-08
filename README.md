# Book Club

A book review website where user's can write and share reviews for specific books.

Created for my Code Institute Backend Development Milestone Project.

A link to the live site can be found [here](https://book-club-rob.herokuapp.com/).
 
## UX
 
### Primary Goals

To create a site where user's can easily write, share and read book reviews and find new books they want to read.

### Developer Goals

- To gain experience using Flask and MongoDB to create a full stack site backed by a well designed database.
- To create a site where I will be able to find new good books to read.

### User Stories

As a reviewer I want:

- An intuitive way to either register a new account or log into my existing account.
- An intuitive form for writing my review so I can easily write a new review including:
    - Star system to score my review out of 5.
    - Large text area to write up my review.
- A way to edit the reviews I have written so I can change them if I notice mistakes or change my mind about something.
- A way to delete reviews I no longer want to be on the website.

As a user (looking to buy a book) I want:

- A home page that displays the most recent reviews on the page so I can quickly see some reviews.
- A page where all the reviews are shown so I can see all the reviews.
- A search bar where I can search for reviews for a specific book I want to read.
- An intuitive layout for the page for each review so I can easily gain all the information I need.
- A way to upvote reviews I think were good so that other users can have an idea of which reviews are good.
- A link from each review to purchase the book so that I can easily buy the book if I decide I want to.

### Wireframes

- [Home Page](static/wireframes/home-page.pdf)
- [Book Page](static/wireframes/book-page.pdf)

## Features
 
### Existing Features

- Home page showing all books in the database, along with their author, cover and average score.
- Search bar on home page to search for a specific book.
- Login and signup functionality for users of the site.
- A page where users can add new reviews to the database. They can write about the book and score them out of 5.
- A page where users can add a new book to the database.
- Buttons on the `add_book` where a user can autofill the information for a book using the Google Books API, either from the book name and author, or the ISBN10.
- A page for each book where the info for that book is displayed (title, author, cover image, description, average score)
- A list of reviews for each book on the book page including score, review author and review text for each review.
- Functionality to edit and delete a book and it's info if you added it to the database or are the admin.
- Functionality to edit and delete a review if you wrote it or are the admin.

### Features Left to Implement

- A profile page where users can see all the reviews they have written and edit and delete them.

## Data Schema

The database was created as a non-relational MongoDB database called "book_club". This database contains 2 collections called "books" (containing all data related to the books and reviews) and "users" (containing all data related to the users of the site).

Items in the "users" collection where structured in the following way:
- _id: The unique id for each user (ObjectId)
- username: The user's unique username (string)
- password: A hash of the user's password (string)
- email: The user's email address (string)

Items in the "books" collection were structured in the following way:
- _id: The unique id for each book (ObjectId)
- book_name: The name of the book (string)
- author: The author of the book (string)
- img_url: The url of the google books cover image for the book (string)
- purchase_link: The url of the amazon link for the book generated from the book's ISBN (string)
- average_score: The average score from the book's reviews (int)
- added_by: The username of the user that added the book (string)
- description: A description of the book (string)
- reviews: An array containing an object for each of the book's reviews (Array)

Each of the review objects in the reviews array were structured in the following way:
- score: The score given to the book in the review (int)
- review_text: The text of the review (string)
- review_author: The username of the author of the review (string)

## Technologies Used

- [HTML5](https://en.wikipedia.org/wiki/HTML#:~:text=Hypertext%20Markup%20Language%20(HTML)%20is,scripting%20languages%20such%20as%20JavaScript.)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [Materialize](https://materializecss.com/)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [JQuery](https://jquery.com)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Flask](https://en.wikipedia.org/wiki/Flask_(web_framework))
- [MongoDB](https://www.mongodb.com/1)
- [Heroku](https://en.wikipedia.org/wiki/Heroku)

## Testing

The testing of the site is documented in [testing.md](testing.md)

## Deployment

The site was deployed on [Heroku](https://heroku.com/) and will automatically update upon new commits pushed to the github repository: [https://github.com/RobKnowles248/book-club](https://github.com/RobKnowles248/book-club).

Since the environment variables stored in `env.py` were not pushed to git these were manually as as config variables on Heroku.

## Credits

### Code

- The script in `signup-validation.js` for checking the passwords match on `signup.html` was adapted from [this jsfiddle](http://jsfiddle.net/SirusDoma/ayf832td/).
- The code for the login and signup forms and methods was adapted from that used in the Code Institute Back End Development "Task Manager" miniproject.

### Acknowledgements

Thanks to my mentor Akshat Garg for his help with building the project.