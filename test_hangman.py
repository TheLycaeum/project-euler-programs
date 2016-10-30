from hangman import secret_word
def test_secret_word():
   word = secret_word()
   assert(word != None)
   assert(len(word)>5)
  

def test_hide_word():
   word="saheed"
   blank_word=hide_word(word)
   assert(len(word)==len(blank_word))
