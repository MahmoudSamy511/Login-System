# importing login and registration functions
from login import login
from Registration import register

print("Hello ,User!!")
try:
    x = int(input("Please enter 1 if you want to Sign in or 2 for Sign up: "))  # Ask user to sign in or sign up
    if x == 1:
        login()
    elif x == 2:
        register()
    else:
        print("Invalid action")
except ValueError as err:        # Error handling
    print(err)
