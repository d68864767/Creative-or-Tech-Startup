```python
class Community:
    def __init__(self):
        # Initialize an empty list of community posts
        self.posts = []

    def add_post(self, post):
        # Add a new post to the list
        self.posts.append(post)

    def remove_post(self, post):
        # Remove a post from the list
        if post in self.posts:
            self.posts.remove(post)

    def display_posts(self):
        # Display all the community posts
        print("Here are the latest community posts:")
        for post in self.posts:
            print(f"- {post}")

    def search_posts(self, keyword):
        # Search for a post by keyword
        print(f"Searching for posts related to '{keyword}'...")
        for post in self.posts:
            if keyword.lower() in post.lower():
                print(f"- {post}")

    def engage(self):
        # Engage with the community
        print("Engaging with the Oceanly community...")
        self.display_posts()
```
