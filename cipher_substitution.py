## Cryptanalisys script for substituting single letters from ciphertext to plaintext

## File access
CIPHER_READ = "cipher1.txt"
CIPHER_WRITE = "cipher1_solved.txt"

## Letters to be swapped
CIPHER_LETTER = "n"
PLAIN_LETTER = "E" ##Use UPPERCASE for plaintext letters so that they don't overlap with cipher letters

f = open(CIPHER_READ, "r")

text = f.read()
f.close()

text = text.replace(CIPHER_LETTER, PLAIN_LETTER)

f = open(CIPHER_WRITE, "w")
f.write(text)
        