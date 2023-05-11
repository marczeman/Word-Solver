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
rack = prep_rack(rack_raw)
min_length = st.number_input('Minimum word length: ', min_value = 2, value = defaults['min_word_length'])
max_length = st.number_input('Maximum word length: ' , min_value = 1, max_value = 15, value = len(''.join(rack)))

button = st.button("Find best words")



if button:

        word_list_twl06 = load_words_online(dict_paths['url_twl06'])
        valid_words = find_words(rack, word_list_twl06, min_length = min_length, max_length= max_length)
        #valid_words.sort(reverse= True, key = len)

        valid_words_df = prep_results(valid_words)

        # Define Streamlit app layout and widgets
        st.markdown("## Possible words:")
        #my_array = np.random.rand(5, 3)
        #st.table(valid_words)
        st.dataframe(valid_words_df)
