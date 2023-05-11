

def prep_rack(rack_raw):
    # Split the input string into a list of strings
    rack = rack_raw.split(',')

    # Strip leading and trailing whitespace from each string in the list
    rack = [s.strip() for s in rack]

    return rack

def prep_rack_dict(rack_raw):

    rack_dict = {s.split('_')[0]: int(s.split('_')[1]) for s in rack_raw}

    return rack_dict
