import pandas as pd

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
