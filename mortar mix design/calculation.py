# calculations.py

from data_storage import get_ratio


def get_numeric_ratio(ratio_string):
    """Convert a ratio string to numeric values."""
    cement, sand = map(int, ratio_string.split(':'))
    return cement, sand


def calculate_materials(cement_type, category, volume, cement_sg, sand_sg):
    """Calculate the amount of cement and sand needed for a given volume."""
    ratio_string = get_ratio(cement_type, category)
    cement_parts, sand_parts = get_numeric_ratio(ratio_string)

    total_parts = cement_parts + sand_parts
    cement_fraction = cement_parts / total_parts
    sand_fraction = sand_parts / total_parts

    # Calculate volumes
    cement_volume = volume * cement_fraction
    sand_volume = volume * sand_fraction

    # Convert to mass using specific gravity
    # Assume water density of 1000 kg/m³
    cement_mass = cement_volume * cement_sg * 1000  # in kg
    sand_mass = sand_volume * sand_sg * 1000  # in kg

    return cement_mass, sand_mass, cement_volume, sand_volume