from user_mod import User

class Privileges:
    """A class to store admin system privileges."""
    def __init__(self, privileges=None):
        if privileges is None:
            self.privileges = ["can add post", "can delete post", "can ban user"]
        else:
            self.privileges = privileges

    def show_privileges(self):
        print("\nAdministrative privileges discovered:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    """An admin class that inherits from User and uses Privileges."""
    def __init__(self, first_name, last_name, username):
        super().__init__(first_name, last_name, username)
        self.privileges = Privileges()
