# Ariel Turchinsky 316614882
# Patrick Lugasi 319266177

with open("text.txt", 'r') as f:
    text = f.read()
    textList = text.split()  # split all of the text to a list of words
word = 0
while (word < len(textList)):  # check for each word if it contains not English letters
    # . , ? ! are special cases, if they appear at the start or end of the word, we do not remove the whole word
    #  but only the . , ? and !
    if not (textList[word].isalpha()):
        if ('.' in textList[word]) and (textList[word].startswith('.') or textList[word].endswith('.')):
            textList[word] = textList[word].replace('.', '')
            word += 1
        elif (',' in textList[word]) and (textList[word].startswith(',') or textList[word].endswith(',')):
            textList[word] = textList[word].replace(',', '')
            word += 1
        elif ('?' in textList[word]) and (textList[word].startswith('?') or textList[word].endswith('?')):
            textList[word] = textList[word].replace('?', '')
            word += 1
        elif ('!' in textList[word]) and (textList[word].startswith('!') or textList[word].endswith('!')):
            textList[word] = textList[word].replace('!', '')
            word += 1
        else:
            textList.remove(textList[word])  # for every other case, remove the whole word
    else:
        word += 1
for index in textList:  # another check after we filtered the . , ? !
    if not (index.isalpha()):
        textList.remove(index)
    textList[textList.index(index)] = index.lower()
newText = ' '.join(textList)  # join the words on the list to a new string

with open("dictionary.txt", 'r')as dictFile:
    evalDict = eval(dictFile.read())


def category(word, dict):
    """
    returns to which category(ies) the word belongs
    :param word: word from the dictionary
    :param dict: the dictionary itself
    :return: if word=check, return the value of the dictionary, else, return {}
    """
    for check in dict:
        if word == check:
            return dict[check]

    return {}


def count(text, word):
    """
    returns how many times the word is in the text
    :param text: the text string
    :param word: word from the text
    :return: how many times the word is in the text
    """
    count = 0
    for occurence in text.split():
        if word == occurence:
            count = count + 1
    return count


sortedList = []
listOfWord = []
for word in newText.split():  # creating a list of item, how many times it's shown and its categories
    if word not in listOfWord:
        listOfWord.append(word)
        sortedList.append(tuple([word, count(newText, word), category(word, evalDict)]))

sortedList.sort(key=lambda list: list[1], reverse=True)  # sorting the list by number of times it's show by reverse
subList = []
alphaList = []


def MaxCount(sortedList):
    """
    returns the maximum number of how many times a word is shown in the text
    :param sortedList: list in the form of (ite,how many times it's shown, categories)
    :return: maximum number of how many times a word is shown in the text
    """
    return sortedList[0][1]


countForSort = MaxCount(sortedList)
while (countForSort > 0):  # sorting by alphabetical order the sub groups of the list
    for index in range(0, len(sortedList)):
        if sortedList[index][1] == countForSort:
            # all the words that have the same amount of appearance will be
            # joined together to the sublist and will be sorted
            subList.append(sortedList[index])
            subList.sort(reverse=True)
    alphaList.extend(subList)  # the sublist will be extended to a bigger list that will contain every sorted sublist
    subList.clear()
    countForSort -= 1
sortedList = alphaList
with open("words.txt", 'w') as file:
    file.write(repr(sortedList))
