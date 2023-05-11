# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import string
import itertools
import requests


def load_words(file_path):
    with open(file_path, 'r') as f:
        return set(line.strip().lower() for line in f)

def load_words_online(url):
    response = requests.get(url)
    word_list_txt = response.text
    # Split text into lines and convert to set of strings
    lines = set(word_list_txt.strip().split('\n'))
    lines = {s.replace('\r', '') for s in lines}
    return lines

def find_words(rack, words, min_length = 2, max_length = None):


    print('Minimum word length is {}'.format(min_length))
    if max_length is None:
        max_length = len(''.join(rack))
    print('Maximum word length is {}'.format(max_length))

    filtered_word_list = set(s for s in words if (len(s) <= max_length) & (len(s) >= min_length))
    # print(list(filtered_word_list)[1])

    alphabet = string.ascii_lowercase


    words_found = set()
    n_blank = rack.count('?') # counting number of blanks

    for combination in itertools.product(alphabet, repeat=n_blank):
        pseudo_rack = []
        i = 0
        for item in rack:
            if item == '?':
                pseudo_rack.append(combination[i])
                i += 1
            else:
                pseudo_rack.append(item)
        # print(pseudo_rack)
        for i in range(1, max_length+1):
            for subset in itertools.permutations(pseudo_rack, i):
                word = ''.join(subset).lower()
                # print(word)
                if word in filtered_word_list:
                    #print("found a word:", word)
                    words_found.add(word)

    words_found_list = list(words_found)
    words_found_list.sort(reverse= True, key=lambda s: (len(s), s))
    return words_found_list

def prep_rack(rack_raw):
    # Split the input string into a list of strings
    rack = rack_raw.split(',')

    # Strip leading and trailing whitespace from each string in the list
    rack = [s.strip() for s in rack]

    return rack

# Define a function to calculate the Scrabble score of a word
def scrabble_score(word):
    score_dict = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2,
                  'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1,
                  'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1,
                  'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10}
    return sum([score_dict[c] for c in word.upper()])

def prep_results(result_list):
    # Create a list of dictionaries, where each dictionary represents a row of data
    data = []
    for word in result_list:
        row_dict = {'Word': word, 'Length': len(word), 'Scrabble Score': scrabble_score(word)}
        data.append(row_dict)

    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(data)
    # Sort the DataFrame by 'Age' and then by 'Salary'
    df_sorted = df.sort_values(['Length', 'Word'], ascending=[False, True]).reset_index(drop=True)


    return df_sorted

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
