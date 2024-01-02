```python
# Import necessary modules
from product_listing import ProductListing
from sustainability import Sustainability
from education import Education
from community import Community

class Oceanly:
    def __init__(self):
        self.product_listing = ProductListing()
        self.sustainability = Sustainability()
        self.education = Education()
        self.community = Community()

    def run(self):
        # Run the main application
        print("Welcome to Oceanly.com - Your online marketplace for ocean-related products and services!")

        # Display product listings
        self.product_listing.display_products()

        # Display sustainability initiatives
        self.sustainability.display_initiatives()

        # Display educational resources
        self.education.display_resources()

        # Engage with the community
        self.community.engage()

if __name__ == "__main__":
    app = Oceanly()
    app.run()
```
