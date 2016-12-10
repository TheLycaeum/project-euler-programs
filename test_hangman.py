from hangman import secret_word,replace_blanks

import tempfile, os

def test_secret_word(tmpdir):
   print (tmpdir)
   fname = tempfile.mktemp()
   with open(fname, "w") as f:
      for i in ["aa", "bbb", "cccccc"]:
         f.write(i+"\n")
   word = secret_word(fname, 5)
   assert word=="cccccc","Wrong word was choosen {}".format(word)  
   os.unlink(fname)
  
   
def test_replace_blanks():
   word="saheed"
   guessed=["e","a"]
   new=replace_blanks(word,guessed)
   assert("*a*ee*"== new)
   
