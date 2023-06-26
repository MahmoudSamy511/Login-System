# Login and Registration System

This is a simple Login and Registration System built using Python. It prompts users to register by providing their first and last name, username, birthdate as a date object, email, and password. The data is stored in a simple txt file.

## Registration

To register, the user is prompted to enter their first and last name, username, birthdate, email, and password. The system validates the input and creates a new user in the database file. The user's data is stored in a comma-separated format, making it easy to retrieve and display the data.

## Database

The user data is stored in a simple txt file. Each line in the file represents a user's data, with each field separated by a comma. The file is created if it does not exist, and new users are appended to the end of the file.

## Login

To log in, the user is prompted to enter either their username or email and their password. The system validates the input and checks whether the data matches a user's data in the database file. If the data matches, the user is logged in, and a welcome message is displayed. If the data does not match, an error message is displayed, and the user is asked to try again.

## Dependencies

This project does not require any external dependencies. It is built using the built-in functions and modules in Python.

## How to Run

To run the Login and Registration System, simply run the `Main.py` file in a Python environment. The system will prompt the user to register or log in, depending on whether the user is already registered or not.

## Conclusion

This simple Login and Registration System built using Python provides a basic framework for building more complex user authentication systems. Its simplicity makes it easy to understand and modify to suit your needs.
