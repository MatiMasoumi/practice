from shop import Shop
def main():
     shop = Shop()
     while True:
          command = input("Enter a command (add, display, remove, edit, search, summary, help, exit): ").strip().lower()
          if command == "add":
             name = input("Enter product name: ")
             price = float(input("Enter product price: "))
             code = input("Enter unique product code: ")
             shop.add_product(name, price, code)
          elif command == "display": 
             shop.display_products()
          elif command == "remove":
             code = input("Enter the unique code of the product to remove: ")
             shop.remove_product(code) 
          elif command == "edit":
             code = input("Enter the unique code of the product to edit: ")
             new_name = input("Enter new name (leave blank to keep current name): ")
             price_input = input("Enter new price (leave blank to keep current price): ") 
             new_price = float(price_input) if price_input else None shop.edit_product(code, new_name if new_name else None, new_price) 
          elif command == "search":
             search_term = input("Enter the product name or code to search: ")
             shop.search_product(search_term)
          elif command == "summary": shop.display_summary()
          elif command == "help": shop.show_help() 
          elif command == "exit":
             print("Exiting the program.") 
             break
          else: print("Invalid command. Please try again.") 
if __name__ == "__main__": main()

