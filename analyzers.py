from loader import load_AFINN, load_rhetoric_words, load_excluded_words

lex = load_AFINN()
rhetoric= load_rhetoric_words()
excluded_words = load_excluded_words()

def word_cleaner(text, exclude_quotes):
    text_list = text.split()
    quote_indeces = []
    counter = 1
    if exclude_quotes == 'yes':
        i = 0 
        while i < len(text_list):
            if '"' in text_list[i] or '“' in text_list[i]:
                quote_indeces.insert(0,i)
                while i+counter < len(text_list) and ('"' not in text_list[i + counter] and '”' not in text_list[i + counter]):
                    quote_indeces.insert(0,i+counter)
                    counter += 1
                i+=counter
                counter = 1
            i+=1

    for i in range(len(quote_indeces)):
        del(text_list[quote_indeces[i]])

    for i in range(len(text_list)):
            text_list[i] = text_list[i].lower().strip(".,!?\"()'")
    return text_list
    

def sentiment_analysis(text):
    word_list = []
    avg = 0
    abs = 0
    hig = 0
    low = 0
    for word in text:
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
    for word in text:
        if word in rhetoric:
            word_list.append(word)
    values = (len(word_list),len(word_list)/len(text.split()),word_list)
    return values

def rhetoric_spotter_v2(text):
    word_counts = {}
    word_ticker = 0

    for word in text:
            if word in rhetoric:
                word_ticker += 1
                word_counts[word] = word_counts.get(word,0)+1
    values = (word_ticker, word_ticker/len(text), word_counts)
    return values

def repitition_spotter(text):
    word_counts = {}
    for word in text:
        if word and word not in excluded_words:
            word_counts[word] = word_counts.get(word,0) + 1
