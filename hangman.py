import random
def secret_word():
    with open("/usr/share/dict/words") as f:
        for i in f:
            i=i.strip()
            if i.isalpha() and len(i)==4:
                return i

