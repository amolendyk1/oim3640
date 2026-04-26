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

def compare_songs(results):
    print("\n==============================================")
    print("              COMPARISON TABLE")
    print("==============================================")
    print(f"{'Song':30} {'Total':>7} {'Unique':>7} {'Ratio':>7}")
    print("----------------------------------------------")

    for name, hist in results.items():
        total = total_words(hist)
        unique = unique_words(hist)
        ratio = unique / total if total > 0 else 0

        # Extract only the filename from the full Windows path
        short_name = name.split("\\")[-1][:28]

        print(f"{short_name:30} {total:7} {unique:7} {ratio:7.2f}")
        
def main():
    songs = ["C:\\Users\\amolendyk1\\Desktop\\oim3640\\data\\talking_to_the_moon.txt", "C:\\Users\\amolendyk1\\Desktop\\oim3640\\data\\when_i_was_your_man.txt", "C:\\Users\\amolendyk1\\Desktop\\oim3640\\data\\too_good_to_say_goodbye.txt", "C:\\Users\\amolendyk1\\Desktop\\oim3640\\data\\put_on_a_smile.txt", "C:\\Users\\amolendyk1\\Desktop\\oim3640\\data\\risk_it_all.txt"]
    
    results = {}
    for filename in songs:
        hist = process_file(filename)
        results[filename] = hist

        print("Total words:", total_words(hist))
        print("Unique words:", unique_words(hist))
        print("Top 10 words:")
        print_top(hist, 10)

    compare_songs(results)

if __name__ == "__main__":
    main()

