```python
class ProductListing:
    def __init__(self):
        # Initialize an empty list of products
        self.products = []

    def add_product(self, product):
        # Add a new product to the list
        self.products.append(product)

    def remove_product(self, product):
        # Remove a product from the list
        if product in self.products:
            self.products.remove(product)

    def display_products(self):
        # Display all the products
        print("Here are our available products:")
        for product in self.products:
            print(f"- {product}")

    def search_products(self, keyword):
        # Search for a product by keyword
        print(f"Searching for products related to '{keyword}'...")
        for product in self.products:
            if keyword.lower() in product.lower():
                print(f"- {product}")
```
