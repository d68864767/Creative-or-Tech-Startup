```python
class UserInterface:
    def __init__(self):
        # Initialize user interface elements
        self.ui_elements = []

    def add_ui_element(self, element):
        # Add a user interface element
        self.ui_elements.append(element)

    def initialize(self):
        # Initialize all user interface elements
        for element in self.ui_elements:
            if not element.is_initialized():
                raise Exception(f"User interface element {element.name} is not initialized!")

        print("User interface is initialized.")

    class UIElement:
        def __init__(self, name):
            self.name = name

        def is_initialized(self):
            # Check if the user interface element is initialized
            # This is a placeholder and should be replaced with actual checks
            return True
```
