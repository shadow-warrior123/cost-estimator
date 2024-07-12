# calculation.py

from data_storage import get_ratio

def get_numeric_ratio(ratio_string):
    """Convert a ratio string to numeric values."""
    mortar, brick = map(int, ratio_string.split(':'))
    return mortar, brick

def calculate_materials(brick_type, bond_type, wall_volume, brick_volume):
    """Calculate the amount of mortar and number of bricks needed for a given volume."""
    ratio_string = get_ratio(brick_type, bond_type)
    mortar_parts, brick_parts = get_numeric_ratio(ratio_string)

    total_parts = mortar_parts + brick_parts
    mortar_ratio = mortar_parts / total_parts
    brick_ratio = brick_parts / total_parts

    mortar_volume = wall_volume * mortar_ratio
    brick_volume_total = wall_volume * brick_ratio

    num_bricks = brick_volume_total / brick_volume

    return mortar_volume, num_bricks

