from string import ascii_lowercase

# one = ['a', 'i']
# two = ['of', 'to', 'in', 'it', 'is', 'be', 'as', 'at', 'so', 'we', 'he', 'by', 'or', 'on', 'do', 'if', 'me', 'my',
#        'up', 'an', 'go', 'no', 'us', 'am']
# three = ['the', 'and', 'for', 'are', 'but', 'not', 'you', 'all', 'any', 'can', 'had', 'her', 'was', 'one', 'our',
#           'out', 'day', 'get', 'has', 'him', 'his', 'how', 'new', 'now', 'old', 'see', 'two', 'way', 'who', 'boy',
#           'did', 'let', 'put', 'say', 'she', 'too']


def decrypt_file():
    key = "bxicl yo dthngavukfwerm ps"

    cipher_text = ""

    with open('data.txt', 'r') as file:
        lines = file.readlines()
        print(lines)
        cipher_text = lines[0]
        print(cipher_text)

    for j in range(len(cipher_text)):
        c = cipher_text[j]
        if c in ascii_lowercase:
            index = ord(c) - 97
            cipher_text = cipher_text[:j] + str(key[index]) + cipher_text[j+1:]

    print("#"*50, "Decrypted Paragraph", "#"*50, "\n")
    print(cipher_text, end="\n")


decrypt_file()
