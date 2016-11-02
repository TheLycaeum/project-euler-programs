from hangman import secret_word,hide_word,replace_blanks
def test_secret_word():
   f=open("/usr/share/dict/words")
   word = secret_word()
   assert(word,f)
   assert(len(word)>5)
  

def test_hide_word():
   word="saheed"
   blank_word = hide_word(word)
   assert('******' == blank_word)

def test_replace_blanks():
   word="saheed"
   guessed="e"
   new=replace_blanks(word,guessed)
   assert(word,guessed)
   assert(new,guessed)
