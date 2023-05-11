
import itertools
import string

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
