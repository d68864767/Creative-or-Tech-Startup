```python
# Import necessary modules
from plant_identification import PlantIdentification
from care_schedule import CareSchedule
from wellness_content import WellnessContent
from community import Community

class Bloomify:
    def __init__(self):
        self.plant_identification = PlantIdentification()
        self.care_schedule = CareSchedule()
        self.wellness_content = WellnessContent()
        self.community = Community()

    def start(self):
        print("Welcome to Bloomify! Your personal gardening and wellness companion.")
        user_input = input("What would you like to do today? \n1. Identify a plant \n2. Check care schedule \n3. Read wellness content \n4. Join the community \n")

        if user_input == '1':
            self.plant_identification.identify_plant()
        elif user_input == '2':
            self.care_schedule.check_schedule()
        elif user_input == '3':
            self.wellness_content.read_content()
        elif user_input == '4':
            self.community.join_community()
        else:
            print("Invalid option. Please choose a number between 1 and 4.")

if __name__ == "__main__":
    app = Bloomify()
    app.start()
```
