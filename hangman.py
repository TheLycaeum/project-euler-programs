import random
def secret_word():
    good_words=[]
    with open("/usr/share/dict/words") as f:
        for i in f:
            i=i.strip()
            if i.isalpha() and len(i)>5:
                good_words.append(i)
    word=random.choice(good_words)
    
    return word
def hide_word(word):
    blanks="*"*len(word)
    return blanks
