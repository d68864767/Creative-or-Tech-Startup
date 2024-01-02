```python
class Sustainability:
    def __init__(self):
        # Initialize an empty list of sustainability initiatives
        self.initiatives = []

    def add_initiative(self, initiative):
        # Add a new initiative to the list
        self.initiatives.append(initiative)

    def remove_initiative(self, initiative):
        # Remove an initiative from the list
        if initiative in self.initiatives:
            self.initiatives.remove(initiative)

    def display_initiatives(self):
        # Display all the sustainability initiatives
        print("Here are our sustainability initiatives:")
        for initiative in self.initiatives:
            print(f"- {initiative}")

    def search_initiatives(self, keyword):
        # Search for an initiative by keyword
        print(f"Searching for initiatives related to '{keyword}'...")
        for initiative in self.initiatives:
            if keyword.lower() in initiative.lower():
                print(f"- {initiative}")
```
