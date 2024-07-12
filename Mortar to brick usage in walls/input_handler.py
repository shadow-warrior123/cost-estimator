# input_handler.py

from data_storage import ratio_data_MB

def get_brick_type():
    """Get the brick type used for wall"""
    while True:
        brick_type_used = input("Enter type of brick size used \n(1. 190x90x90 (brick) \n2. 600x300x200 (AAC block)): ")
        if brick_type_used == "1":
            return "Brick"
        elif brick_type_used == "2":
            return "AAC"
        print("Invalid input. Please enter 1 for Brick or 2 for AAC block.")

def get_bond(brick_type_used):
    """Get the bond type from user input."""
    while True:
        print(f"Available bond types for {brick_type_used}:")
        for bond_type in ratio_data_MB[brick_type_used]:
            print(f"- {bond_type}")
        bond_type = input("Enter bond type: ")
        if bond_type in ratio_data_MB[brick_type_used]:
            return bond_type
        print("Invalid bond type. Please try again.")

def get_volume():
    """Get the wall volume from user input."""
    while True:
        try:
            volume = float(input("Enter wall volume in cubic meters: "))
            if volume > 0:
                return volume
            print("Volume must be a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_brick_dimensions(brick_type):
    """Get the brick dimensions based on the brick type."""
    if brick_type == "Brick":
        return 190, 90, 90  # mm
    else:  # AAC
        return 600, 300, 200  # mm