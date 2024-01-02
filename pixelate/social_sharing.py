```python
class SocialSharing:
    def __init__(self):
        self.photo = None

    def load_photo(self):
        photo_path = input("Enter the path of the photo you want to share: ")
        try:
            self.photo = open(photo_path, 'r')  # This is a placeholder. In a real scenario, you would use a library like PIL to open the image.
            print("Photo loaded successfully.")
        except FileNotFoundError:
            print("File not found. Please enter a valid path.")

    def share_photo(self):
        if self.photo is None:
            print("No photo loaded. Please load a photo first.")
            self.load_photo()

        while True:
            print("\n1. Share on Facebook\n2. Share on Instagram\n3. Share on Twitter\n4. Share via Email\n5. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.share_on_facebook()
            elif choice == 2:
                self.share_on_instagram()
            elif choice == 3:
                self.share_on_twitter()
            elif choice == 4:
                self.share_via_email()
            elif choice == 5:
                print("Photo shared successfully.")
                break
            else:
                print("Invalid choice. Please choose a valid option.")

    def share_on_facebook(self):
        print("Sharing photo on Facebook...")  # This is a placeholder. In a real scenario, you would use a library or API to perform the operation.

    def share_on_instagram(self):
        print("Sharing photo on Instagram...")  # This is a placeholder. In a real scenario, you would use a library or API to perform the operation.

    def share_on_twitter(self):
        print("Sharing photo on Twitter...")  # This is a placeholder. In a real scenario, you would use a library or API to perform the operation.

    def share_via_email(self):
        print("Sharing photo via Email...")  # This is a placeholder. In a real scenario, you would use a library or API to perform the operation.
```
