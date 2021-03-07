## Cryptanalisys script for letter frequency analysis

import numpy as np

## File access
CIPHER_READ = "cipher1.txt"
CIPHER_WRITE = "cipher1_solved.txt"

f = open(CIPHER_READ, "r")

word_frequencies = {}
letter_frequencies = {}

text = f.read() ##Should try to set all letters to be lowercase
f.close()

## Letter frequency analysis
for char in text:
    if char in letter_frequencies:
        letter_frequencies[char] += 1
    else:
        letter_frequencies[char] = 1
letter_frequencies.pop(" ") ## Remove spaces from list, as they are not part of cryptanalysis
total_letters = sum(letter_frequencies.values(), 0.0) ## Convert int value to float to retain precision when dividing
percentage_frequencies = {k: (v / total_letters * 100) for k, v in letter_frequencies.items()}

## Word frequency analysis
text = text.split()
for word in text:
    if word in word_frequencies:
        word_frequencies[word] += 1
    else:
        word_frequencies[word] = 1


## Arrange words and letters in descending order accroding to frequency of appearance.
sort_letter_frequencies = sorted(percentage_frequencies.items(), key=lambda x: x[1], reverse=True)
sort_word_frequencies = sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True)

print("Letter frequencies in cipher text: ")
print(sort_letter_frequencies)
print(int(total_letters), "letters in total.\n")

print("Word frequencies in cipher text: ")
print(sort_word_frequencies)
print(len(sort_word_frequencies), "words in total.\n")

## IC calculation 
frequencies_values = np.zeros(len(letter_frequencies))
total_values = np.zeros(len(letter_frequencies))
i = 0
for word in letter_frequencies:
    total_values[i] = letter_frequencies.get(word)
    frequencies_values[i] = (letter_frequencies.get(word))**2
    i += 1

print("IC calculation for cipher text: ")
print(frequencies_values)
print(np.sum(frequencies_values))
print(np.sum(total_values))
print(np.sum(frequencies_values)/(np.sum(total_values)**2))

        