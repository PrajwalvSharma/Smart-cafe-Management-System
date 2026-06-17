import mysql.connector

# Data Base Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin@123",
    database="cafe_db"
)

cursor = db.cursor()


# ➕ Add Item
def add_item():
    name = input("Enter item name: ")
    price = float(input("Enter price: "))

    # Check duplicate item
    cursor.execute(
        "SELECT * FROM menu WHERE item_name=%s",
        (name,)
    )

    existing_item = cursor.fetchone()

    if existing_item:
        print("❌ Item already exists!")

    else:
        cursor.execute(
            "INSERT INTO menu (item_name, price) VALUES (%s, %s)",
            (name, price)
        )

        db.commit()

        print("✅ Item added successfully!")


# ❌ Remove Item
def remove_item():
    view_menu()

    item_id = int(input("\nEnter item ID to remove: "))

    cursor.execute(
        "SELECT * FROM menu WHERE id=%s",
        (item_id,)
    )

    item = cursor.fetchone()

    if item:
        cursor.execute(
            "DELETE FROM menu WHERE id=%s",
            (item_id,)
        )

        db.commit()

        print("✅ Item removed successfully!")

    else:
        print("❌ Invalid item ID")


# 📋 View Menu
def view_menu():
    cursor.execute("SELECT * FROM menu")

    items = cursor.fetchall()

    print("\n===== MENU =====")

    if len(items) == 0:
        print("No items available")

    else:
        for item in items:
            print(f"ID: {item[0]} | {item[1]} | ₹{item[2]}")


# 🧾 Place Order
def place_order():
    view_menu()

    item_id = int(input("\nEnter item ID: "))
    quantity = int(input("Enter quantity: "))

    cursor.execute(
        "SELECT item_name, price FROM menu WHERE id=%s",
        (item_id,)
    )

    result = cursor.fetchone()

    if result:
        name, price = result

        total = price * quantity

        cursor.execute(
            "INSERT INTO orders (item_id, quantity, total_price) VALUES (%s, %s, %s)",
            (item_id, quantity, total)
        )

        db.commit()

        print("\n🧾 ===== BILL =====")
        print(f"Item Name : {name}")
        print(f"Price     : ₹{price}")
        print(f"Quantity  : {quantity}")
        print(f"Total     : ₹{total}")

    else:
        print("❌ Invalid item ID")


# 🔄 Reset Menu and IDs
def reset_menu():
    confirm = input("Do you want to reset menu data? (yes/no): ")

    if confirm.lower() == "yes":

        cursor.execute("DELETE FROM orders")
        cursor.execute("DELETE FROM menu")

        cursor.execute("ALTER TABLE menu AUTO_INCREMENT = 1")
        cursor.execute("ALTER TABLE orders AUTO_INCREMENT = 1")

        db.commit()

        print("✅ Menu reset successfully!")

    else:
        print("❌ Reset cancelled")


# 🧠 Main Menu
def main():

    while True:

        print("\n===== SMART CAFE SYSTEM =====")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Menu")
        print("4. Place Order")
        print("5. Reset Menu")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_item()

        elif choice == "2":
            remove_item()

        elif choice == "3":
            view_menu()

        elif choice == "4":
            place_order()

        elif choice == "5":
            reset_menu()

        elif choice == "6":
            print("🙏 Thank you!")
            break

        else:
            print("❌ Invalid choice")


# Run Program
main()