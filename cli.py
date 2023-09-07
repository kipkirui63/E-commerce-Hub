import click
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model import Base, Customer, Product, Sale, Inventory, InventoryAlert, User, OrderDetail

# Define the base class for declarative models
Base = declarative_base()

# Set up the database connection
DATABASE_URL = "sqlite:///analytics.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def cli():
    pass

# def generate_table_cli(table, table_name, fields):
#     @click.command(name=f"add-{table_name.lower()}")
#     def add_item():
#         try:
#             item_data = {}
#             for field in fields:
#                 item_data[field] = click.prompt(f"{field.capitalize()}", type=str)
#             new_item = table(**item_data)
#             session.add(new_item)
#             session.commit()
#             click.echo(f"Added {table_name}: {new_item}")
#         except Exception as e:
#             session.rollback()
#             click.echo(f"Error: {str(e)}")

#     @click.command(name=f"delete-{table_name.lower()}")
#     @click.option("--id", prompt=f"Enter {table_name} ID to delete", type=int, help=f"{table_name} ID to delete")
#     def delete_item(id):
#         item = session.query(table).filter(getattr(table, f"{table_name.lower()}_id") == id).first()
#         if item:
#             session.delete(item)
#             session.commit()
#             click.echo(f"Deleted {table_name} with ID {id}")
#         else:
#             click.echo(f"{table_name} with ID {id} not found.")

#     @click.command(name=f"update-{table_name.lower()}")
#     @click.option("--id", prompt=f"Enter {table_name} ID to update", type=int, help=f"{table_name} ID to update")
#     def update_item(id):
#         item = session.query(table).filter(getattr(table, f"{table_name.lower()}_id") == id).first()
#         if item:
#             update_data = {}
#             for field in fields:
#                 new_value = click.prompt(f"New {field.capitalize()}", default=getattr(item, field))
#                 update_data[field] = new_value
#             for field, value in update_data.items():
#                 setattr(item, field, value)
#             session.commit()
#             click.echo(f"Updated {table_name} with ID {id}")
#         else:
#             click.echo(f"{table_name} with ID {id} not found.")

#     @click.command(name=f"list-{table_name.lower()}s")
#     def list_items():
#         items = session.query(table).all()
#         if items:
#             click.echo(f"List of {table_name}s:")
#             for item in items:
#                 item_data = ", ".join([f"{field.capitalize()}: {getattr(item, field)}" for field in fields])
#                 click.echo(item_data)
#         else:
#             click.echo(f"No {table_name.lower()}s found.")

#     return add_item, delete_item, update_item, list_items

# customer_cli = generate_table_cli(Customer, "Customer", ["customer_name", "email", "phone_number"])
# product_cli = generate_table_cli(Product, "Product", ["product_name", "description", "price"])
# sale_cli = generate_table_cli(Sale, "Sale", ["customer_id", "product_id", "order_date", "quantity_sold", "unit_price"])
# inventory_cli = generate_table_cli(Inventory, "Inventory", ["product_id", "quantity_in_stock"])
# inventory_alert_cli = generate_table_cli(InventoryAlert, "InventoryAlert", ["product_id", "alert_date", "threshold_quantity", "current_quantity"])
# user_cli = generate_table_cli(User, "User", ["username", "password_hash", "role"])
# order_detail_cli = generate_table_cli(OrderDetail, "OrderDetail", ["order_id", "product_id", "quantity", "subtotal"])

# if __name__ == "__main__":
#     for command in customer_cli:
#         cli.add_command(command)
#     for command in product_cli:
#         cli.add_command(command)
#     for command in sale_cli:
#         cli.add_command(command)
#     for command in inventory_cli:
#         cli.add_command(command)
#     for command in inventory_alert_cli:
#         cli.add_command(command)
#     for command in user_cli:
#         cli.add_command(command)
#     for command in order_detail_cli:
#         cli.add_command(command)

#     cli()
