words = input('Enter a sentence : ')
dct = dict()
for word in words:
    if word not in dct:
        dct[word]=words.count(word)
print(dct)
