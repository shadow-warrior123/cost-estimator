# input_handler.py

from data_storage import cement_data

def get_cement_type():
    """Get the cement type from user input."""
    while True:
        cement_type = input("Enter cement type (OPC_33, OPC_43, OPC_53, PPC, PSC): ").upper()
        if cement_type in cement_data:
            return cement_type
        print("Invalid cement type. Please try again.")

def get_category(cement_type):
    """Get the category from user input."""
    while True:
        print(f"Available categories for {cement_type}:")
        for category in cement_data[cement_type]:
            print(f"- {category}")
        category = input("Enter category: ")
        if category in cement_data[cement_type]:
            return category
        print("Invalid category. Please try again.")

def get_volume():
    """Get the volume from user input."""
    while True:
        try:
            volume = float(input("Enter volume in cubic meters: "))
            if volume > 0:
                return volume
            print("Volume must be a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_specific_gravity(material):
    """Get the specific gravity of a material from user input."""
    while True:
        try:
            sg = float(input(f"Enter specific gravity of {material}: "))
            if sg > 0:
                return sg
            print("Specific gravity must be a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")