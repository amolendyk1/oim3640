def uses_only(word, letters):
    """Does word use only the allowed letters?"""
    for letter in word:
        if letter not in letters:
            return False
    return True

def uses_all(word, letters):
    """Does word use all necessary letters?"""
    for letter in words:
        if letter not in letters:
            return False
    return True

def uses_all(word, letters):
    """Does word use long enough letters?"""
    for letter in word:
        if letter not in letters:
            return False
    return True

def find_words(letters, required):
    """Finds words that use only the allowed letters and include the center letter."""
    with open("C:\\Users\\amolendyk1\\Desktop\\oim3640\\data\\words.txt", "r") as word_file:
        for word in word_file:
            word = word.strip()
            if uses_only(word, letters) and uses_all(word, required):
                print(word)
