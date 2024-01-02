```python
# Import necessary modules
from photo_editing import PhotoEditing
from ai_filters import AIFilters
from social_sharing import SocialSharing
from learning_hub import LearningHub

class Pixelate:
    def __init__(self):
        self.photo_editing = PhotoEditing()
        self.ai_filters = AIFilters()
        self.social_sharing = SocialSharing()
        self.learning_hub = LearningHub()

    def start(self):
        print("Welcome to Pixelate.io - Your one-stop platform for all your photo editing needs!")
        while True:
            print("\n1. Edit Photo\n2. Apply AI Filters\n3. Share Photo\n4. Visit Learning Hub\n5. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.photo_editing.edit_photo()
            elif choice == 2:
                self.ai_filters.apply_filter()
            elif choice == 3:
                self.social_sharing.share_photo()
            elif choice == 4:
                self.learning_hub.access_resources()
            elif choice == 5:
                print("Thank you for using Pixelate.io. Happy editing!")
                break
            else:
                print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    pixelate = Pixelate()
    pixelate.start()
```
