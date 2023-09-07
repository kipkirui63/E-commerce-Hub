from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Customer, Product, Sale, Inventory, InventoryAlert, User, OrderDetail
from datetime import date

# database connection URL
DATABASE_URL = 'sqlite:///analytics.db'

# Create the database engine
engine = create_engine(DATABASE_URL)

# Create the tables in the database.
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

def seed_data():
    # Seed Customers
    customer1 = Customer(customer_name="Alexis", email="macalister@example.com", phone_number="123-456-7890")
    customer2 = Customer(customer_name="Sczobozlai", email="sczobozlai@example.com", phone_number="987-654-3210")

    # Seed Products
    product1 = Product(product_name="Milk", description="Perishable", price=19.99)
    product2 = Product(product_name="Gasoline", description="Non Perishable", price=29.99)

    # Seed Sales
    sale1 = Sale(customer=customer1, product=product1, order_date=date(2023, 1, 15), quantity_sold=3, unit_price=19.99)
    sale2 = Sale(customer=customer2, product=product2, order_date=date(2023, 1, 20), quantity_sold=2, unit_price=29.99)

    # Seed Inventory
    inventory1 = Inventory(product=product1, quantity_in_stock=50)
    inventory2 = Inventory(product=product2, quantity_in_stock=30)

    # Seed Inventory Alerts 
    alert1 = InventoryAlert(product=product1, alert_date=date(2023, 1, 10), threshold_quantity=10, current_quantity=5)
    alert2 = InventoryAlert(product=product2, alert_date=date(2023, 1, 12), threshold_quantity=15, current_quantity=8)

    # Seed Users 
    user1 = User(username="admin", password_hash="admin@254", role="admin")
    user2 = User(username="user", password_hash="user@254", role="user")

    # Seed Order Details
    order_detail1 = OrderDetail(sale=sale1, product=product1, quantity=3, subtotal=59.97)
    order_detail2 = OrderDetail(sale=sale2, product=product2, quantity=2, subtotal=59.98)

    # Add data to the session
    session.add_all([customer1, customer2, product1, product2, sale1, sale2, inventory1, inventory2, alert1, alert2, user1, user2, order_detail1, order_detail2])
    session.commit()

# if __name__ == "__main__":
#     seed_data()
