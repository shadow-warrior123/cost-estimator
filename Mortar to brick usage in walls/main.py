# main.py

from input_handler import get_brick_type, get_bond, get_volume, get_brick_dimensions
from calculation import calculate_materials

def main():
    print("Brick Wall Material Calculator")

    brick_type = get_brick_type()
    bond_type = get_bond(brick_type)
    wall_volume = get_volume()
    brick_length, brick_width, brick_height = get_brick_dimensions(brick_type)
    
    brick_volume = (brick_length * brick_width * brick_height) / 1_000_000_000  # Convert to cubic meters

    mortar_volume, num_bricks = calculate_materials(brick_type, bond_type, wall_volume, brick_volume)

    print(f"\nResults:")
    print(f"Mortar volume used: {mortar_volume:.3f} cubic meters")
    print(f"Number of bricks used: {num_bricks:.0f}")

if __name__ == "__main__":
    main()