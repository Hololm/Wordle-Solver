from english_words import english_words_lower_alpha_set as dictionary


if __name__ == "__main__":

    # only words that are 5 chars
    for i in dictionary.copy():
        if len(i) != 5:
            dictionary.remove(i)

    class Wordle:
        def __init__(self, word: str, green: str, yellow: str, gray: str):
            self.word = word
            self.green = green
            self.yellow = yellow
            self.gray = gray

        def gray_solve(self):
            for ele in self.gray:
                for dict_word in dictionary.copy():
                    if ele in dict_word:
                        dictionary.remove(dict_word)
            return dictionary

    player_word = Wordle("first", 'f', 'i', 'rst')
    print(player_word.gray_solve())

