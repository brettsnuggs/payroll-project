import User as u

def user_validate(user_list):
    while True:
        username = input("\nUsername: ")
        password = input("Password: ")

        for dicts in user_list:
            if username == dicts['user_id']:
                if password == dicts['password']:
                    print(f"\nWelcome, {username}!")
                    return dicts['auth_code']
                else:
                    print("Invalid username or password")
                    continue


def login():
    user_list = u.read_file()  # reads file
    print("\nWelcome to the Employee Payroll Portal\n")

    while True:
        opt = input(f"'L' to login or 'R' to register: ")

        if opt.lower() == 'l':
            auth_code = user_validate(user_list)
            u.print_users(user_list)
            return auth_code

        elif opt.lower() == 'r':
            u.create_user(user_list)
            u.print_users(user_list)
            break
        else:
            continue