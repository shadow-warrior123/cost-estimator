from input_handler import get_cement_type, get_category, get_volume, get_specific_gravity
from calculation import calculate_materials


def main():
    print("Welcome to the Cement Calculator")

    cement_type = get_cement_type()
    category = get_category(cement_type)
    volume = get_volume()
    cement_sg = get_specific_gravity("cement")
    sand_sg = get_specific_gravity("sand")

    cement_mass, sand_mass, cement_volume, sand_volume = calculate_materials(
        cement_type, category, volume, cement_sg, sand_sg
    )

    print(f"\nResults:")
    print(f"Cement needed: {cement_mass:.2f} kg ({cement_volume:.2f} m³)")
    print(f"Sand needed: {sand_mass:.2f} kg ({sand_volume:.2f} m³)")


if __name__ == "__main__":
    main()