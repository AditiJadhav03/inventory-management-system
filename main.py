
from database import connect

# ---------------- ADD PRODUCT ----------------
def add_product():
    conn = connect()
    cursor = conn.cursor()

    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    low_stock = int(input("Enter low stock alert level: "))

    cursor.execute("""
        INSERT INTO products (name, price, quantity, low_stock_level)
        VALUES (?, ?, ?, ?)
    """, (name, price, quantity, low_stock))

    conn.commit()
    conn.close()

    print("✅ Product added successfully!")


# ---------------- VIEW PRODUCTS ----------------
def view_products():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    print("\nID | Name | Price | Quantity")
    print("--------------------------------------")

    for p in products:
        print(f"{p[0]} | {p[1]} | ₹{p[2]} | {p[3]}")

    conn.close()


# ---------------- UPDATE QUANTITY ----------------
def update_quantity():
    conn = connect()
    cursor = conn.cursor()

    product_id = int(input("Enter product ID to update: "))
    new_quantity = int(input("Enter new quantity: "))

    cursor.execute("UPDATE products SET quantity = ? WHERE id = ?", (new_quantity, product_id))
    conn.commit()

    if cursor.rowcount == 0:
        print("❌ Product not found.")
    else:
        print("✅ Quantity updated successfully!")

    conn.close()


# ---------------- SEARCH PRODUCT ----------------
def search_product():
    conn = connect()
    cursor = conn.cursor()

    name = input("Enter product name to search: ")

    cursor.execute("SELECT * FROM products WHERE name LIKE ?", ('%' + name + '%',))
    results = cursor.fetchall()

    if results:
        print("\nFound Products:")
        for r in results:
            print(f"ID:{r[0]} | {r[1]} | ₹{r[2]} | Stock:{r[3]}")
    else:
        print("❌ No product found.")

    conn.close()


# ---------------- RECORD SALE ----------------
def record_sale():
    conn = connect()
    cursor = conn.cursor()

    product_id = int(input("Enter product ID sold: "))
    sold_qty = int(input("Enter quantity sold: "))

    cursor.execute("SELECT quantity FROM products WHERE id = ?", (product_id,))
    result = cursor.fetchone()

    if result:
        current_qty = result[0]

        if sold_qty > current_qty:
            print("❌ Not enough stock!")
        else:
            new_qty = current_qty - sold_qty
            cursor.execute("UPDATE products SET quantity = ? WHERE id = ?", (new_qty, product_id))
            conn.commit()
            print("✅ Sale recorded!")
    else:
        print("❌ Product not found.")

    conn.close()


# ---------------- LOW STOCK ALERT ----------------
def low_stock_alert():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name, quantity, low_stock_level
        FROM products
        WHERE quantity <= low_stock_level
    """)

    items = cursor.fetchall()

    print("\n⚠ LOW STOCK PRODUCTS:")
    if not items:
        print("All products are sufficiently stocked.")
    else:
        for item in items:
            print(f"{item[0]} - Remaining Stock: {item[1]}")

    conn.close()


# ---------------- MENU ----------------
def menu():
    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Quantity")
    print("4. Search Product")
    print("5. Record Sale")
    print("6. Low Stock Alert")
    print("7. Exit")


# ---------------- MAIN LOOP ----------------
while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        view_products()

    elif choice == "3":
        update_quantity()

    elif choice == "4":
        search_product()

    elif choice == "5":
        record_sale()

    elif choice == "6":
        low_stock_alert()

    elif choice == "7":
        print("Thank you for using Inventory System 👋")
        break

    else:
        print("Invalid choice. Try again.")
