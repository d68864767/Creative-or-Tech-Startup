```python
class PhotoEditing:
    def __init__(self):
        self.photo = None

    def load_photo(self):
        photo_path = input("Enter the path of the photo you want to edit: ")
        try:
            self.photo = open(photo_path, 'r')  # This is a placeholder. In a real scenario, you would use a library like PIL to open the image.
            print("Photo loaded successfully.")
        except FileNotFoundError:
            print("File not found. Please enter a valid path.")

    def edit_photo(self):
        if self.photo is None:
            print("No photo loaded. Please load a photo first.")
            self.load_photo()

        while True:
            print("\n1. Crop\n2. Rotate\n3. Adjust Brightness\n4. Adjust Contrast\n5. Save and Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.crop_photo()
            elif choice == 2:
                self.rotate_photo()
            elif choice == 3:
                self.adjust_brightness()
            elif choice == 4:
                self.adjust_contrast()
            elif choice == 5:
                self.save_photo()
                print("Photo edited successfully.")
                break
            else:
                print("Invalid choice. Please choose a valid option.")

    def crop_photo(self):
        print("Cropping photo...")  # This is a placeholder. In a real scenario, you would use a library like PIL to perform the operation.

    def rotate_photo(self):
        print("Rotating photo...")  # This is a placeholder. In a real scenario, you would use a library like PIL to perform the operation.

    def adjust_brightness(self):
        print("Adjusting brightness...")  # This is a placeholder. In a real scenario, you would use a library like PIL to perform the operation.

    def adjust_contrast(self):
        print("Adjusting contrast...")  # This is a placeholder. In a real scenario, you would use a library like PIL to perform the operation.

    def save_photo(self):
        print("Saving photo...")  # This is a placeholder. In a real scenario, you would use a library like PIL to save the image.
```
