# Loads the AFINN-111 lexicon (Finn Årup Nielsen, ODbL v1.0)
# See README for full attribution.
def load_AFINN():
    lexicon = {}
    with open("data/AFINN-111.txt") as f:
        for line in f:
            word,score = line.split("\t")
            lexicon[word] = int(score)
    return lexicon

def load_rhetoric_words():
    words = set()
    with open("data/rhetoric_words.txt") as f:
        for line in f:
            word = line.strip().lower()
            if word:
                words.add(word)
    return words