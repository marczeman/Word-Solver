#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 17:58:00 2023

@author: marcparrikal
"""

import streamlit as st
import numpy as np
from functions import load_words_online, prep_rack, find_words, scrabble_score, prep_results
from config import paths, default_rack

st.title('Scrabble Solver')


# Get user input

rack_raw = st.text_input('Enter your rack (comma separated):', value = default_rack)
rack = prep_rack(rack_raw)
min_length = st.number_input('Minimum word length: ', 2)
max_length = st.number_input('Maximum word length: ' , min_value = 1, max_value = 15, value = len(''.join(rack)))

button = st.button("Find best words")

if button:



    word_list_twl06 = load_words_online(paths['url_twl06'])
    valid_words = find_words(rack, word_list_twl06, min_length = min_length, max_length= max_length)
    #valid_words.sort(reverse= True, key = len)

    valid_words_df = prep_results(valid_words)

    # Define Streamlit app layout and widgets
    st.markdown("## Possible words:")
    #my_array = np.random.rand(5, 3)
    #st.table(valid_words)
    st.dataframe(valid_words_df)
