# You are given a string of length N and a parameter k. The string can be manipulated by taking one of the first k letters and moving it to the end

def alterWord(word, words, k):
    # Remove k characters from word
    for x in range(0, k):
        character = word[x]
        word = word[k:]
        words.append(character)

    # Append k characters from words array to string
    for x in words:
        word += x

    print(word)


alterWord("daily", [], 1)
