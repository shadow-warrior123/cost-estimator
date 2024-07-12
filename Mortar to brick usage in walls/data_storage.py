ratio_data_MB = {
    'Brick': {
        'Stretcher Bond': '1:5',
        'Flemish Bond': '1:4',
        'English Bond': '1:3'
    },
    'AAC': {
        'Stretcher Bond': '1:5',
        'Flemish Bond': '1:4',
        'English Bond': '1:3'
    }
}

def get_ratio(brick_type, bond_type):
    """Get the mortar:brick ratio for given bond type and category"""
    try:
        return ratio_data_MB[brick_type][bond_type]
    except KeyError:
        return "Ratio not found for the given brick type and bond type."