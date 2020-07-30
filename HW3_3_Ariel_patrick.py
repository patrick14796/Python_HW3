# Ariel Turchinsky 316614882
# Patrick Lugasi 319266177

with open("words.txt", 'r') as file:
    sortedTuples = eval(file.read())
wordDict = {}
for word in sortedTuples:  # sorting the tuples in a way that at least one of terms exists and writing the reasons for
    # the filtering
    if word[1] >= 5:
        wordDict[word[0]] = 'Because it appears at list five times'
    if len(word[2]) > 1:
        if word[1] >= 5:
            wordDict[word[0]] = 'Because it belongs to at least two categories and it appears at list five times'
        else:
            wordDict[word[0]] = 'Because it belongs to at least two categories'
for k, v in wordDict.items():
    print(f"'{k}' {v}")
