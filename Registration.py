import datetime
import bcrypt
import ast


def register():
    """...This Is A Registration Function..."""
    k = j = d = 0
    first_n = input("Please Enter your first name: ")
    last_n = input("Please Enter your last name: ")
    user = input("Please Enter your username: ")
    f1 = open("Data_Base.txt", 'r')  # Opening database file for read
    rows = f1.readlines()  # storing data in database into list
    for a in range(0, len(rows)):
        # Reading each line in database
        x = rows[a]
        # Convert each element in list into dict
        d1 = ast.literal_eval(x)
        if user == d1['username']:  # Checking if username exist already in database or not
            print("<<Username already exist>>")
            register()
    if user[0].isdigit():  # Checking if username starting with number
        print("<< username can't start with number >>")
        register()
    else:
        try:
            birth_date = input("Please enter your date of birth (dd/mm/yyyy) : ")  # Ask user for his date of birth
            # storing date of birth in form {dd-mm-yy-00-00-00}
            date = datetime.datetime.strptime(birth_date, '%d/%m/%Y')
            birth_d = str(datetime.date(date.year, date.month, date.day))  # storing date of birth in form{yyy-mm-dd}
            if date.year > 2022:  # check birth year
                print("<<<Invalid date of birth>>>")
                register()
            else:
                age = datetime.datetime.now().year - date.year  # calculate age of user from his birthday
                email = input("Please Enter your e-mail: ")
                # checking for valid email
                if len(email) >= 6:  # confirm that the email is not short
                    if email[0].isalpha():  # check if the first index is an alphabet
                        if ("@" in email) and (email.count("@") == 1):  # check if mail contain {@}or not
                            if (email[-4] == ".") ^ (email[-3] == "."):  # check if [.] exist or not
                                for i in email:
                                    if i == i.isspace():  # check if mail contain space or not
                                        k = 1
                                    elif i.isalpha():  # check if mail contain capital alphabet or not
                                        if i == i.upper():
                                            j = 1
                                    elif i.isdigit():
                                        continue
                                    elif i == "_" or i == "." or i == "@":
                                        continue
                                    else:
                                        d = 1
                                    # warning user for his mistake
                                if k == 1 or j == 1 or d == 1:
                                    print("<<Wrong Email>>")
                                    register()
                            else:
                                print("<<Wrong Email>>")
                                register()
                        else:
                            print("<<Wrong Email>>")
                            register()
                    else:
                        print("<<Wrong Email>>")
                        register()
                else:
                    print("<<Wrong Email>>")
                    register()
                password = input("Please input your desired password: ")
                password_con = input("Please input your desired password again: ")
                # check if password and password_con are equal
                if password != password_con:
                    print("<<Check the password again>>")
                    register()
                    # check if password less than 8 characters or not
                elif len(password) < 8:
                    print("<<Password is too short>>")
                    register()
                else:
                    file = open("Data_Base.txt", 'a')  # Opening database file for append
                    # encrypting the user password
                    pass1 = password.encode('utf-8')
                    f_pass = (bcrypt.hashpw(pass1, bcrypt.gensalt())).decode('utf8')
                    # storing date of user into database as dictionary
                    data = dict(First_name=first_n, Last_name=last_n, username=user, Birthday=birth_d, Email=email,
                                Password=f_pass, Age=age)
                    file.write(str(data) + "\n")
                    print("<<<You have signed up successfully!!>>>")
                    file.close()  # closing file
                    quit()
            # Error handling
        except ValueError as err:
            print(err)
            register()


