
import itertools
import string

def find_words(rack, words, min_length = 2, max_length = None, early_stop = False, n_best = None, first_letter = None, last_letter = None):


    filtered_word_list = set(s for s in words if (len(s) <= max_length) & (len(s) >= min_length))
    # print(list(filtered_word_list)[1])
    if first_letter is not None:
        filtered_word_list = {s for s in filtered_word_list if s[0] == first_letter}

    if last_letter is not None:
        filtered_word_list = {s for s in filtered_word_list if s[-1] == last_letter}

    alphabet = string.ascii_lowercase


    words_found = set()
    n_blank = rack.count('?') # counting number of blanks

    stopping_flag = False
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
        for i in range(max_length, 0, -1): # start with larger permutations so can stop early if find big word
            for subset in itertools.permutations(pseudo_rack, i):
                word = ''.join(subset).lower()
                # print(word)
                if word in filtered_word_list:
                    #print("found a word:", word)
                    words_found.add(word)
                    if early_stop == True and len(words_found) >= n_best:
                        stopping_flag = True
                        break
            if stopping_flag:
                break
        if stopping_flag:
                break

    words_found_list = list(words_found)
    words_found_list.sort(reverse= True, key=lambda s: (len(s), s))
    return words_found_list
