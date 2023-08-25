string = "dog cat hello cat dog dog hello cat g g g g g g world"
word1 = "hello"
word2 = "world"

words = string.split(' ')

occurences = {word1: [], word2: []}
for pos, word in enumerate(words):
    if word == word1:
        occurences[word1].append(pos)
    elif word == word2:
        occurences[word2].append(pos)

print(occurences)

best = 1000000
winner1 = 0
winner2 = 0
for each in occurences[word1]:
    for all in occurences[word2]:
        if each < all and (all - each) < best:
            best = (all - each) - 1
            winner1 = each
            winner2 = all

print(f"Winning combo! --> {winner1} - {winner2}")
print(f"Number of words in between --> {best}")