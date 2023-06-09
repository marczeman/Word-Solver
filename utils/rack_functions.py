import streamlit as st

def prep_rack(rack_raw):
    bad_rack_flag = False
    # Split the input string into a list of strings
    rack = rack_raw.split(',')

    # Strip leading and trailing whitespace from each string in the list
    rack = [s.strip() for s in rack]
    n_blank = rack.count('?')
    if n_blank > 3:
        st.error("Currently supports only up to 3 blanks(?) ")
        bad_rack_flag = True
    return rack, n_blank, bad_rack_flag

def prep_rack_dict(rack_raw):

    rack_dict = {s.split('_')[0]: int(s.split('_')[1]) for s in rack_raw}

    return rack_dict
