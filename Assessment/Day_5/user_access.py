def require_admin(func):
    def wrapper(user, *args, **kwargs):
        if user != "admin":
            print("Access denied")
            return
        return func(user, *args, **kwargs)
    return wrapper

@require_admin
def delete_user(user, user_id):
    print(f"User {user_id} deleted by {user}")

delete_user("guest", 101)
delete_user("admin", 101)
