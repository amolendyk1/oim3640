import string 

def process_file(filename):
    hist = {}
    fp = open(filename, encoding = "utf-8")

    for line in fp:
        for word in line.split():
        word = word.strip(string.punctuation).lower()
        if word:
            hist[word] = hist.get(word, 0) + 1
        return hist

def total_words(hist):
    return sum(hist.values())

def unique_words(hist):
    return len(hist)

def most_common(hist):
    t = []
    for word, freq in hist.items():
        t.append((freq, word))
    t.sort(reverse = True)
    return t

def print_top(hist, n=10):
    t = most_common(hist)
    for freq, word in t[:n]:
        print(freq, word)

def main():
    filename = 
    hist = process_file(filename)
    print("Total words:", total_words(hist))
    print("Unique words:", unique_words(hist))
    print("\nTop 10 words:")
    print_top(hist, 10)

if__name__ == "__main__":
    main()

