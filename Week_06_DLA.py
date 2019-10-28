# 11.1

fin = open('words.txt')

def word_to_dicty():
    dicty = dict()
    for line in fin:
        word = line.strip()
        dicty[word] = word
    return dicty

## print word_to_dicty() #DO NOT RUN

# 12.1

def most_frequent(word):
    dicty = dict()
    for letter in word:
        dicty[letter] = dicty.get(letter, 0) + 1
    return dicty

print (most_frequent('bannana'))
