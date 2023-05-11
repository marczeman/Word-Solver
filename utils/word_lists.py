# -*- coding: utf-8 -*-
import requests
import streamlit as st

@st.cache
def load_words(file_path):
    with open(file_path, 'r') as f:
        return set(line.strip().lower() for line in f)
@st.cache
def load_words_online(url):
    response = requests.get(url)
    word_list_txt = response.text
    # Split text into lines and convert to set of strings
    lines = set(word_list_txt.strip().split('\n'))
    lines = {s.replace('\r', '') for s in lines}
    return lines






# if __name__ == '__main__':
#     rack_raw = input("Enter your letters (comma separated): ")
#     min_length = input("Minimum word length: ")

#     max_length = input("Maximum word length: ")


#     rack = prep_rack(rack_raw)
#     min_length = 2 if min_length == '' else min_length
#     max_length = len(''.join(rack_raw)) if max_length == '' else max_length
#     print(rack)
#     word_list = load_words_online(paths['url_twl06'])
#     valid_words = find_words(rack, word_list, min_length = int(min_length), max_length= int(max_length))
#     valid_words.sort(reverse= True, key = len)
#     print("Valid words:", valid_words)
