#inventory to store products
inventory=[]

#function to insert a new product
def insert_product():
    sku = input("Enter SKU: ")
    # check for duplicate SKU
    for item in inventory:
        if item['SKU'] == sku:
            print("Product with this SKU is already listed.")
            return
    name = input("Enter the name: ")
    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid quantity. Please enter a number.")
        return
    # create a new product dictionary
    product = {'SKU': sku, 'Name': name, 'Quantity': quantity}
    inventory.append(product)
    print("Product added successfully.")

        #Display the inventory
def update_product():
    sku = input("Enter SKU of the product to update: ")
    for item in inventory:
        if item['SKU'] == sku:
            print(f"Current details: Name: {item['Name']}, Quantity: {item['Quantity']}")
            new_name = input("Enter new name (leave blank to keep current): ")
            if new_name:
                item['Name'] = new_name
            try:
                new_quantity = input("Enter new quantity (leave blank to keep current): ")
                if new_quantity:
                    item['Quantity'] = int(new_quantity)
            except ValueError:
                print("Invalid quantity. Keeping current value.")
            print("Product updated successfully.")
            return
    print("Product with this SKU not found.")
def display_inventory():
    if not inventory:
        print("Inventory is empty.")
        return
    print("Current Inventory:")
    for item in inventory:
        print(f"SKU: {item['SKU']}, Name: {item['Name']}, Quantity: {item['Quantity']}")
    print()

    # Main program loop
def main():
    while True:
        print("\nInventory Stock Manager")
        print("1. Insert New Product")
        print("2. Display Inventory")
        print("3. Update Product Details")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            insert_product()
        elif choice == '2':
            display_inventory()
        elif choice == '3':
            update_product()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the program
main()
