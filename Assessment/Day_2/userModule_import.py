import UserModule

# Write a menudriven program to add user information and display all user information

print("Welcome to the user information system")
print("Press 1 to Add user information")
print("Press 2 to Display all the user information")
print("Press 3 to Exit")

while True:
    choice = int(input("Enter your choice:"))
    if choice == 1:
        user_id = int(input("Enter the user id:"))
        user_name = input("Enter the user name:")
        user_email = input("Enter the user email:")
        UserModule.add_user_info(user_id, user_name, user_email)
        print("User Information added successfully")
    elif choice == 2:
        all_user_info = UserModule.get_all_user_info()
        print("All User information:")
        for user_id, user_info in all_user_info.items():
            print(f"User ID: {user_id}, Name: {user_info['user_name']}, Email: {user_info['user_email']}")
    elif choice == 3:
        print("Exiting the program")
        break
    else:
        print("Invalid choice")