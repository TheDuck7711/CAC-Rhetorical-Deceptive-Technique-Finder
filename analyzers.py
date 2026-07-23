from loader import load_AFINN, load_rhetoric_words

lex = load_AFINN()
rhetoric= load_rhetoric_words()

def sentiment_analysis(text):
    word_list = []
    avg = 0
    abs = 0
    hig = 0
    low = 0
    for word in text.split():
        word = word.lower().strip(".,!?\"()'")
        if word in lex:
            word_list.append(word)

    if word_list:
        pos = lex[word_list[0]]
        neg = lex[word_list[0]]

    for word in word_list:
        temp_val = lex[word]
        if temp_val < 0:
            abs = abs - temp_val
            avg = avg + temp_val 
        else:
            abs = abs + temp_val
            avg = avg + temp_val
        if hig < temp_val:
                hig = temp_val
        if low > temp_val:
                low = temp_val

    if word_list:
        avg = avg / len(word_list)
        abs = abs / len(word_list)
    values =  (abs,avg,hig,low)
    return values

def rhetoric_spotter(text):
    word_list = []
    for word in text.split():
            word = word.lower().strip(".,!?\"()'")
            if word in rhetoric:
                word_list.append(word)
    values = (len(word_list),len(word_list)/len(text.split()),word_list)
    return values