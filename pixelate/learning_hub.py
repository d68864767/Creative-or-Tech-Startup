```python
class LearningHub:
    def __init__(self):
        self.resources = {
            'Tutorials': ['Basic Photo Editing', 'Advanced Photo Editing', 'Using AI Filters', 'Sharing Photos'],
            'Articles': ['Understanding Photo Composition', 'The Art of Black and White Photography', 'The Future of AI in Photography'],
            'Videos': ['Photo Editing for Beginners', 'Mastering AI Filters', 'Creating Stunning Photos with Pixelate.io']
        }

    def access_resources(self):
        while True:
            print("\n1. Tutorials\n2. Articles\n3. Videos\n4. Back to Main Menu")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.display_resources('Tutorials')
            elif choice == 2:
                self.display_resources('Articles')
            elif choice == 3:
                self.display_resources('Videos')
            elif choice == 4:
                print("Returning to the main menu.")
                break
            else:
                print("Invalid choice. Please choose a valid option.")

    def display_resources(self, resource_type):
        print(f"\n{resource_type}:")
        for i, resource in enumerate(self.resources[resource_type], start=1):
            print(f"{i}. {resource}")
        print("\n")
```
