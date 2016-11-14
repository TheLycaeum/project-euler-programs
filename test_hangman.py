from hangman import secret_word,replace_blanks
def test_secret_word():
   fname = "/home/saheed/project-euler-programs/text"
   with open(fname, "w") as f:
      for i in ["aa", "bbb", "cccccc"]:
         f.write(i+"\n")
   word = secret_word(fname, 5)
   assert word=="cccccc","Wrong word was choosen {}".format(word)  
  
   
def test_replace_blanks():
   word="saheed"
   guessed=["e","a"]
   new=replace_blanks(word,guessed)
   assert("*a*ee*"== new)
   
