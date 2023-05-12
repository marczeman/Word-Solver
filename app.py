#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 17:58:00 2023

@author: marcparrikal
"""

import streamlit as st
import numpy as np
from utils.word_lists import load_words_online, load_words
from utils.word_finder import find_words
from utils.rack_functions import prep_rack, prep_rack_dict
from utils.results import prep_results, scrabble_score
from config import dict_paths, defaults, img_paths

word_list_twl06 = load_words_online(dict_paths['url_twl06'])

col1, col2 = st.columns(2)

with col1:
    st.title('Paperback Helper')

with col2:
    # Display game cover
    st.image(img_paths['cover_image'], width=150, caption='Paperback cover', use_column_width=False)

with st.expander("See description"):

    st.markdown('### This tool is an aid for the word game [Paperback](https://boardgamegeek.com/boardgame/141572/paperback).')
    st.write('This is also available as a [mobile app](https://play.google.com/store/apps/details?id=net.fowers.paperbackvol2&hl=en&gl=US)!')
    st.write('Just input your rack as comma separated values. For example, the following rack (including the common letter) can be input as:')
    st.markdown('### \" **i,?,l,s,st,r** \"')
    st.image(img_paths['sample_rack'], width=700, caption='A sample rack from the mobile app version', use_column_width=True)


# Get user input

rack_raw = st.text_input('Enter your rack (comma separated):', value = defaults['default_rack'], key = 'raw')
rack, n_blank = prep_rack(rack_raw)

col3, col4, col5 = st.columns(3)
with col3:
    max_length = st.number_input('Maximum word length: ' , min_value = 1, max_value = 15, value = len(''.join(rack)))
with col4:
    min_length = st.number_input('Minimum word length: ', min_value = 2, value = max_length-2)
with col5:
    early_stop_input = st.checkbox('Early stop?', value = True if n_blank > 2 else False, help = 'For more than 2 blanks(?), it\'s best to stop early')
    if early_stop_input:
        n_best_input = st.number_input('\"Best\" N words: ', value = 7, help = 'Not really the best, just first few good words')
    else:
        n_best_input = 10000000


with st.expander("See advanced options"):
    col6, col7, col8 = st.columns(3)
    with col6:
        first_letter_condition = st.checkbox('First letter condition', value = False, help = 'Only consider words with a particular first letter')
        if first_letter_condition:
            first_letter_input = st.text_input('First letter must be: ', value = rack[0], max_chars=1, help = 'Make sure it\'s part of your rack!')
            first_letter = first_letter_input.lower()
        else:
            first_letter = None
    with col7:
        last_letter_condition = st.checkbox('Last letter condition', value = False, help = 'Only consider words with a particular last letter')
        if last_letter_condition:
            last_letter_input = st.text_input('Last letter must be: ', value = rack[-1], max_chars=1, help = 'Make sure it\'s part of your rack!')
            last_letter = last_letter_input.lower()
        else:
            last_letter = None


calc_button = st.button("Find best words")
if calc_button:
        valid_words = find_words(rack, word_list_twl06,
                                 min_length = min_length, max_length= max_length,
                                 early_stop = early_stop_input, n_best = n_best_input,
                                 first_letter = first_letter, last_letter = last_letter)
        valid_words_df = prep_results(valid_words)

        st.markdown("## Possible words:")
        #my_array = np.random.rand(5, 3)
        #st.table(valid_words)
        st.dataframe(valid_words_df)
