# Ariel Turchinsky 316614882
# Patrick Lugasi 319266177


listFiles = ['cities.txt', 'colors.txt', 'fruit.txt', 'names.txt']
groups = {}  # dictionary that contains {word:set(category)}


def showCategories(file):
    """
    Takes the items from the file, sets them as the key for the dictionary and puts their categories as values for the
    keys
    :param file: text file
    :return: None
    """
    lines = open(file, 'r').readlines()
    withoutTxt = file.partition('.')[0]  # cuts the ".txt" from the string
    for key in lines:
        listOfKeys = key.split()  # splits every line into a list of words (keys)
        for word in listOfKeys:  # removes all the words that contains not English characters
            if not (word.isalpha()):
                listOfKeys.remove(word)

        def buildGroups(key):
            """
            Builds the dictionary of {item: {category set}}
            :param key: key of the dictionary
            :return: None
            """
            key = key.lower()
            categories = set()
            if key in groups:
                groups[key].add(withoutTxt)
            else:
                categories.add(withoutTxt)
                groups[key] = categories

        list(map(buildGroups, listOfKeys))


list(map(showCategories, listFiles))

with open("dictionary.txt", 'w') as f:
    f.write(repr(groups))  # writnig the representaion of the dictionary to a new file
