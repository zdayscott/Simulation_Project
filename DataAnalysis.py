import csvParser
from collections import Counter

tweets = csvParser.ImportTrumpData()

def Vocabulary():
    words = tweets.split(' ')
    words.remove('@b@')

    counts = Counter(words)
    print(counts.most_common(15))

if __name__ == "__main__":
    Vocabulary()

