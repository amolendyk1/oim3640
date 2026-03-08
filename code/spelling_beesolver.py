def uses_only(word, letters):
    """Does word use only the allowed letters?"""
    for letter in word:
        if letter not in letters:
            return False
    return True

def uses_necessary(word, required):
    """Does word use all necessary letters?"""
    for letter in word:
        if letter == required:
            return True
    return False

def accepted_words(word, letters, required):
    """Is it an accepted word?"""
    return uses_only(word, letters) and uses_necessary(word, required) and len(word) >= 4

def find_words(letters, required):
    """Finds words that use only the allowed letters and include the center letter."""
    valid_words = []
    with open("C:\\Users\\amolendyk1\\Desktop\\oim3640\\data\\words.txt") as word_file:
        for word in word_file:
            word = word.strip()
            if accepted_words(word, letters, required):
                valid_words.append(word)
    return valid_words

def total(letters, required):
    words = find_words(letters, required)
    print(words)

if __name__ == "__main__":
    letters = "kcboela"
    required = "a"
    total(letters, required)