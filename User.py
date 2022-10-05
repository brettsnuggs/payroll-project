# Brett Snuggs, CIS261, Part 4
import csv

# globals
file = 'login_info.txt'
fieldnames = ['user_id', 'password', 'auth_code']



def read_file():
    login_creds = []
    with open(file, 'r', newline='') as f:

        reader = csv.DictReader(f, fieldnames=fieldnames, delimiter='|')
        next(reader)
        for line in reader:
            login_creds.append(line)
        return login_creds


def file_append(user):
    with open(file, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter='|')
        writer.writerow(user)

def create_user(user_list):
    user_id = create_id(user_list)
    user_pw = create_pw()
    user_code = get_auth_code()
    user = {
        'user_id': user_id,
        'password': user_pw,
        'auth_code': user_code
    }
    user_list.append(user)  # add user to list
    file_append(user)  # write user to file

def create_id(user_list):
    usernames = [user['user_id'] for user in user_list]
    while True:
        user_id = input("Username: ")
        if len(user_id) == 0:
            continue
        if user_id in usernames:
            print("Username is already taken.")
            continue
        else:
            return user_id


def create_pw():
    while True:
        password = input("Password: ")
        if len(password) == 0 or len(password) < 5:
            print("Password is too short, try again.")
            continue
        else:
            return password


def get_auth_code():
    while True:
        auth_code = input("Enter authorization: 'Admin' or 'User'\n")
        if auth_code.lower() == 'admin':
            access = admin_auth()
            if access:
                return auth_code
            else:
                continue
        if auth_code.lower() == 'user':
            return auth_code


def admin_auth():
    admin_pw = '200675965'
    pw = input("Enter admin authorization code: ")
    if pw == admin_pw:
        print("Access granted.")
        return True
    else:
        print("Access denied.")
        return False


def print_users(user_list):
    print(f"\nusernames  | passwords  | auth_code")
    for user in user_list:
        print(f"{user['user_id']:12} {user['password']:12} {user['auth_code']:4}")