import re


def analyze():
    text = []
    one_letter_word = {}
    two_letter_word = {}
    three_letter_word = {}

    with open("data.txt", "r") as file:
        lines = file.readlines()
        line = lines[0]
        line = re.sub(",", " ", line)
        line = re.sub("\.+", " ", line)
        line = re.sub("\!+", " ", line)
        line = re.sub(" +", " ", line)
        text = line.split(" ")

        for word in text:
            if len(word) == 1:
                one_letter_word = count_freq(one_letter_word, word)
            if len(word) == 2:
                two_letter_word = count_freq(two_letter_word, word)
            if len(word) == 3:
                three_letter_word = count_freq(three_letter_word, word)

        print_freq(one_letter_word, "One Letter Frequency")
        print_freq(two_letter_word, "Two Letter Frequency")
        print_freq(three_letter_word, "Three Letter Frequency")

        letter_freq = {}
        for letter in line:
            if letter in letter_freq:
                letter_freq[letter] = letter_freq[letter] + 1
            else:
                letter_freq[letter] = 1

        print("*" * 30, "Individual Character", "*" * 30, "\n")
        for letter in sorted(letter_freq.keys()):
            print(letter, ": ", letter_freq[letter], end=" | ")
        print("\n\n", "_" * 100)


def count_freq(freq={}, word=""):
    if word in freq:
        freq[word] = freq[word]+1
    else:
        freq[word] = 1
    return freq


def print_freq(freq={}, header=""):
    print("\n", "*"*30, header, "*"*30)
    print()
    for key in sorted(freq.keys()):
        print(key, ": ", freq[key], end=" | ")
    print("\n\n", "_"*50)


analyze()

