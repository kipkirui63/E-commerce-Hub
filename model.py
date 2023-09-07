from sqlalchemy import Column, Integer, String, DECIMAL, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Define the base class for declarative models
Base = declarative_base()

# Define the Customer model
class Customer(Base):
    __tablename__ = 'customers'

    customer_id = Column(Integer, primary_key=True)
    customer_name = Column(String)
    email = Column(String)
    phone_number = Column(String)

    # Define a one-to-many relationship with Sales
    sales = relationship('Sale', back_populates='customer')

Define the Product model
class Product(Base):
    __tablename__ = 'products'
    
    product_id = Column(Integer, primary_key=True)
    product_name = Column(String)
    description = Column(String)
    price = Column(DECIMAL)
    
    # Define a one-to-many relationship with Sales
    sales = relationship('Sale', back_populates='product')
    
#     # Define a one-to-one relationship with Inventory
#     inventory = relationship('Inventory', uselist=False, back_populates='product')

#     # Define a one-to-many relationship with InventoryAlert
#     inventory_alerts = relationship("InventoryAlert", back_populates="product")

#       # Define a one-to-many relationship with OrderDetail
#     order_details = relationship('OrderDetail', back_populates='product')




# # Define the Sale model
# class Sale(Base):
#     __tablename__ = 'sales'
    
#     order_id = Column(Integer, primary_key=True)
#     customer_id = Column(Integer, ForeignKey('customers.customer_id'))
#     product_id = Column(Integer, ForeignKey('products.product_id'))
#     order_date = Column(Date)
#     quantity_sold = Column(Integer)
#     unit_price = Column(DECIMAL)
    
#     # Define many-to-one relationships with Customer and Product
#     customer = relationship('Customer', back_populates='sales')
#     product = relationship('Product', back_populates='sales')

#     # Define a one-to-many relationship with OrderDetail
#     order_details = relationship('OrderDetail', back_populates='sale')

# # Define the Inventory model
# class Inventory(Base):
#     __tablename__ = 'inventory'
    
#     product_id = Column(Integer, ForeignKey('products.product_id'), primary_key=True)
#     quantity_in_stock = Column(Integer)
    
#     # Define a one-to-one relationship with Product
#     product = relationship('Product', back_populates='inventory')

# # Define the InventoryAlert model (optional)
# class InventoryAlert(Base):
#     __tablename__ = 'inventory_alerts'
    
#     alert_id = Column(Integer, primary_key=True)
#     product_id = Column(Integer, ForeignKey('products.product_id'))
#     alert_date = Column(Date)
#     threshold_quantity = Column(Integer)
#     current_quantity = Column(Integer)
    
#     # Define a many-to-one relationship with Product
#     product = relationship('Product', back_populates='inventory_alerts')

# # Optional: Define the User model (if implementing user authentication)
# class User(Base):
#     __tablename__ = 'users'
    
#     user_id = Column(Integer, primary_key=True)
#     username = Column(String)
#     password_hash = Column(String)
#     role = Column(String)

# # Optional: Define the OrderDetail model 
# class OrderDetail(Base):
#     __tablename__ = 'order_details'
    
#     order_detail_id = Column(Integer, primary_key=True)
#     order_id = Column(Integer, ForeignKey('sales.order_id'))
#     product_id = Column(Integer, ForeignKey('products.product_id'))
#     quantity = Column(Integer)
#     subtotal = Column(DECIMAL)
    
#     # Define many-to-one relationships with Sale and Product
#     sale = relationship('Sale', back_populates='order_details')
#     product = relationship('Product', back_populates='order_details')

#      # Define many-to-one relationship with Product
#     product_id = Column(Integer, ForeignKey('products.product_id'))
#     product = relationship('Product', back_populates='order_details')
