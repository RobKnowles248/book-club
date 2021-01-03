# Testing

## Testing the signup form on `signup.html`:

- When the form is submitted with no username, it prompts you to fill in the username.
![Screenshot of no username](static/images/testing/no-username.png)
- When the form is submitted with a username that is too short it prompts you to change the length of the username.
![Screenshot of too short username](static/images/testing/username-too-short.png)
- The form does not let you type a username longer than 15 characters.
- When the form is submitted with a username that already exists a flash message appears saying the username already exists.
![Screenshot of username already exists flash message](static/images/testing/username-exists.png)
- When the form is submitted with no email, it prompts you to fill in the email.
![Screenshot of no email](static/images/testing/no-email.png)
- When the form is submitted with an invalid email, it prompts you to provide a valid email.
![Screenshot of invalid email](static/images/testing/incorrect-email.png)
- When the form is submitted with no password field, it prompts you to fill in the password.
![Screenshot of no password](static/images/testing/no-password.png)
- When the form is submitted with a password that is too short, it prompts you to change the length of the password.
![Screenshot of too short password](static/images/testing/password-too-short.png)
- The form does not let you type a password longer than 15 characters.
- When the form is submitted without filling in the confirm password field it prompts you to fill it in.
![Screenshot of no confirmed password](static/images/testing/no-confirm.png)
- When the form is submitted without matching passwords a flash message appears to say this.
![Screenshot of passwords not matching flash message](static/images/testing/passwords-not-match.png)
- When the form is submitted with all the correct validation, the new user is added to the database and logged into the page.

## Testing the login form on `login.html`:

- When the form is submitted with no username, it prompts you to fill in the username.
![Screenshot of no username](static/images/testing/no-login-username.png)
- When the form is submitted with no password, it prompts you to fill in the password.
![Screenshot of no password](static/images/testing/no-login-password.png)
- When the form is submitted with a username that does not exist, it provides a flash message and reloads.
![Screenshot of flash message](static/images/testing/incorrect-username-or-password.png)
- When the form is submitted with the incorrect password, it provides a flash message and reloads.
![Screenshot of flash message](static/images/testing/incorrect-username-or-password.png)
- When the form is submitted with a correct username and password it logs you in and redirects to the home page.

## Testing logout functionality:

- When the user is logged in and clicks "logout" they are successfully logged out and redirected to the home page.
![Screenshot of successful logout](static/images/testing/logout-test.png)