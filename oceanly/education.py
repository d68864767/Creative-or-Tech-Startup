```python
class Education:
    def __init__(self):
        # Initialize an empty list of educational resources
        self.resources = []

    def add_resource(self, resource):
        # Add a new educational resource to the list
        self.resources.append(resource)

    def remove_resource(self, resource):
        # Remove an educational resource from the list
        if resource in self.resources:
            self.resources.remove(resource)

    def display_resources(self):
        # Display all the educational resources
        print("Here are our educational resources:")
        for resource in self.resources:
            print(f"- {resource}")

    def search_resources(self, keyword):
        # Search for an educational resource by keyword
        print(f"Searching for resources related to '{keyword}'...")
        for resource in self.resources:
            if keyword.lower() in resource.lower():
                print(f"- {resource}")
```
