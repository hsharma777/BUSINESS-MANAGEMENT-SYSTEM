import datetime

# Product class
class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        self.stock += quantity

    def reduce_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        else:
            print("Insufficient stock!")
            return False

# Customer class
class Customer:
    def __init__(self, customer_id, name, contact):
        self.customer_id = customer_id
        self.name = name
        self.contact = contact

# Sale class
class Sale:
    def __init__(self, sale_id, product, customer, quantity):
        self.sale_id = sale_id
        self.product = product
        self.customer = customer
        self.quantity = quantity
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.total_price = product.price * quantity

# Business Management System
class BusinessManagementSystem:
    def __init__(self):
        self.products = []
        self.customers = []
        self.sales = []
        self.product_id_counter = 1
        self.customer_id_counter = 1
        self.sale_id_counter = 1

    # Add Product
    def add_product(self):
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        stock = int(input("Enter product stock: "))
        product = Product(self.product_id_counter, name, price, stock)
        self.products.append(product)
        self.product_id_counter += 1
        print(f"Product '{name}' added successfully!")

    # View Products
    def view_products(self):
        if not self.products:
            print("No products available.")
        else:
            print("\nAvailable Products:")
            for p in self.products:
                print(f"ID: {p.product_id}, Name: {p.name}, Price: ${p.price}, Stock: {p.stock}")

    # Add Customer
    def add_customer(self):
        name = input("Enter customer name: ")
        contact = input("Enter customer contact: ")
        customer = Customer(self.customer_id_counter, name, contact)
        self.customers.append(customer)
        self.customer_id_counter += 1
        print(f"Customer '{name}' added successfully!")

    # View Customers
    def view_customers(self):
        if not self.customers:
            print("No customers available.")
        else:
            print("\nCustomers List:")
            for c in self.customers:
                print(f"ID: {c.customer_id}, Name: {c.name}, Contact: {c.contact}")

    # Record a Sale
    def record_sale(self):
        self.view_products()
        product_id = int(input("\nEnter Product ID to sell: "))
        quantity = int(input("Enter quantity: "))

        selected_product = next((p for p in self.products if p.product_id == product_id), None)
        if not selected_product:
            print("Invalid Product ID!")
            return

        if not selected_product.reduce_stock(quantity):
            return

        self.view_customers()
        customer_id = int(input("\nEnter Customer ID: "))
        selected_customer = next((c for c in self.customers if c.customer_id == customer_id), None)
        if not selected_customer:
            print("Invalid Customer ID!")
            return

        sale = Sale(self.sale_id_counter, selected_product, selected_customer, quantity)
        self.sales.append(sale)
        self.sale_id_counter += 1
        print(f"Sale recorded: {quantity} x {selected_product.name} sold to {selected_customer.name}")

    # View Sales Report
    def sales_report(self):
        if not self.sales:
            print("No sales recorded.")
        else:
            print("\nSales Report:")
            total_revenue = 0
            for s in self.sales:
                print(f"Sale ID: {s.sale_id}, Product: {s.product.name}, Customer: {s.customer.name}, "
                      f"Quantity: {s.quantity}, Total: ${s.total_price}, Date: {s.date}")
                total_revenue += s.total_price
            print(f"\nTotal Revenue: ${total_revenue}")

# Main Function
def main():
    system = BusinessManagementSystem()

    while True:
        print("\n--- Business Management System ---")
        print("1. Add Product")
        print("2. View Products")
        print("3. Add Customer")
        print("4. View Customers")
        print("5. Record Sale")
        print("6. Sales Report")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            system.add_product()
        elif choice == '2':
            system.view_products()
        elif choice == '3':
            system.add_customer()
        elif choice == '4':
            system.view_customers()
        elif choice == '5':
            system.record_sale()
        elif choice == '6':
            system.sales_report()
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
