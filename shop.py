from product import Product
class Shop:
     def __init__(self):
          self.products = {}
     def add_product(self, name, price, code):
         if code in self.products:
             print("Error: Product code must be unique.")
             return
         self.products[code] = Product(name, price, code)
         print("Product added successfully.")
     def display_products(self):
         if not self.products:
             print("No products available.")
             return
             for product in self.products.values():
                 print(product)
     def remove_product(self, code):
         if code in self.products:
             del self.products[code] 
             print("Product removed successfully.")
         else: print("Error: Product not found.")
     def edit_product(self, code, new_name=None, new_price=None):
         if code in self.products:
             if new_name:
                 self.products[code].name = new_name
                 if new_price is not None:
                     self.products[code].price = new_price
                     print("Product updated successfully.")
                 else: print("Error: Product not found.")
     def search_product(self, search_term):
         for product in self.products.values():
             if product.code == search_term or product.name.lower() == search_term.lower():
                 print("Product found:", product)
                 return print("Error: Product not found.")
     def display_summary(self):
         total_products = len(self.products)
         total_value = sum(product.price for product in self.products.values())
         print(f"Total products: {total_products}, Total value: {total_value:.2f}")
     def show_help(self): 
        help_text = """ Available commands: add - Add a new product display - Display all products
          remove - Remove a product by its code edit - Edit a product's details search - 
          Search for a product by name or code summary - Display total products and value help 
          - Show this help message exit - Exit the program """ 
        print(help_text)
