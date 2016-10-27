from hangman import secret_word
def test_secret_word():
   word = secret_word()
   assert(word != None)
   assert(len(word)==4)

