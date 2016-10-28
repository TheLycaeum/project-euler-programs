import random
def secret_word():
    with open("/usr/share/dict/words") as f:
        for i in f:
            i=i.strip()
            if i.isalpha() and len(i)>5:
                return i

def hide_word():
  word=secret_word()  
  blanks="*"*len(word)
  return blanks
