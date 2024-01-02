```python
# Import necessary modules
import getpass

class Community:
    def __init__(self):
        # Initialize a list of all registered users
        self.users = self.load_users()

    def load_users(self):
        # This function should load all registered users from a database or a file
        # For the sake of this example, we will use a list of dummy users
        return ['User 1', 'User 2', 'User 3', 'User 4', 'User 5']

    def user_login(self):
        # This function should handle user login or signup
        # For the sake of this example, we will ask for a username and check if it's in the list of users
        username = input('Please enter your username: ')

        if username in self.users:
            print(f'Welcome back, {username}!')
        else:
            print(f'Welcome, {username}! Your account has been created.')
            self.users.append(username)

        return username

    def engage(self, user):
        # This function should handle community engagement
        # For the sake of this example, we will just print a message
        print(f'Thank you for using Harmonize, {user}! Feel free to share your playlist with the community.')
```
