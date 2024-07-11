# data storage file

cement_data = {
    'OPC 33': {
        'Brickwork load bearing': '1:4',
        'Brickwork non load bearing': '1:5',
        'Plastering (Inner Walls)': '1:4',
        'Plastering (Outer Walls)': '1:5',
        'Flooring': '1:3',
        'Ceiling': '1:3'
    },
    'OPC 43': {
        'Brickwork load bearing': '1:5',
        'Brickwork non load bearing': '1:6',
        'Plastering (Inner Walls)': '1:5',
        'Plastering (Outer Walls)': '1:6',
        'Flooring': '1:4',
        'Ceiling': '1:3'
    },
    'OPC 53': {
        'Brickwork load bearing': '1:6',
        'Brickwork non load bearing': '1:7',
        'Plastering (Inner Walls)': '1:6',
        'Plastering (Outer Walls)': '1:7',
        'Flooring': '1:5',
        'Ceiling': '1:4'
    },
    'PPC': {
        'Brickwork load bearing': '1:5',
        'Brickwork non load bearing': '1:6',
        'Plastering (Inner Walls)': '1:5',
        'Plastering (Outer Walls)': '1:6',
        'Flooring': '1:4',
        'Ceiling': '1:3'
    },
    'PSC': {
        'Brickwork load bearing': '1:5',
        'Brickwork non load bearing': '1:6',
        'Plastering (Inner Walls)': '1:5',
        'Plastering (Outer Walls)': '1:6',
        'Flooring': '1:4',
        'Ceiling': '1:3'
    }
}

def get_ratio(cement_type, category):
    """Get the cement:sand ratio for a given cement type and category."""
    try:
        return cement_data[cement_type][category]
    except KeyError:
        return "Ratio not found for the given cement type and category."
