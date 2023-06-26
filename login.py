# importing ask and base modules
import ast
import bcrypt


def login():
    """...This Is A Login Function..."""
    file1 = open("Data_Base.txt", 'r')  # opening Data base file for read
    lines = file1.readlines()  # storing data in database into list
    user = input("Enter username or email:")
    password = str(input("Enter your password:"))
    check = password.encode('utf-8')
    for i in range(0, len(lines)):
        # Reading each line in database
        x = lines[i]
        # Convert each element in list into dict
        t = ast.literal_eval(x)
        z = str(t['Password']).encode('utf-8')
        # check if username or email and password are exist
        if (user == t['username'] or user == t['Email']) and bcrypt.checkpw(check, z):
            return print("Login successful! \n"), print("welcome!,", t['First_name'])
    return print("<<Invalid username or password>>")


