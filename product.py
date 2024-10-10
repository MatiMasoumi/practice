class Product:
     def __init__(self, name, price, code):
         self.name = name
         self.price = price
         self.code = code
     def __str__(self):
         return f"Name: {self.name}, Price: {self.price}, Code: {self.code}"