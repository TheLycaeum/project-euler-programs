import random
def secret_word(word_file = "/usr/share/dict/words", length = 5):
    good_words=[]
    with open(word_file) as f:
        for i in f:
            i=i.strip()
            if i.isalpha() and len(i)>=length:
                good_words.append(i)
    word=random.choice(good_words)
   
    return word



guessed=[]

def replace_blanks(word,guessed):
    new_blanks=''.join([letter if letter in guessed else '*' for letter in word])
    return new_blanks

def main_function():
    word=secret_word()
    blanks="*"*len(word)
    print(blanks)
    count=10
    wrong_guesses=[]
    while count!=0:
        #for guess in word:
        guess=input("Enter a guess:")
        if guess in word:
            guessed.append(guess)
            print("secret word contains:",guess)
            new_word=replace_blanks(word,guessed)       
            print("word:",new_word)
            if new_word==word:
                print("####congratulation####! The word was :",word)
                break
            
        else:
            if guess not in word:
                wrong_guesses.append(guess)
                count-=1
                print("wrong guesses:",wrong_guesses)
                print("Turns remaining:",count)
               
    

if __name__=='__main__':
   
    main_function()
