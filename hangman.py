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

def replace_blanks(word,guessed):
    new_blanks=''.join([letter if letter in guessed else '*' for letter in word])
    return new_blanks

def main_function():
    guessed=[] 
    word=secret_word()
    print("*"*len(word))  
    count=10
    wrong_guesses=[]
    while count!=0:
            
        guess = input('Enter a guess:')
        if guess=='':
            continue
        if guess in guessed or guess in wrong_guesses:
            print("!!!You already guessed the letter!!!!:",guess)
            print("word:",replace_blanks(word,guessed))
        elif guess in word:
            guessed.append(guess)
            print("secret word contains:",guess)
            new_word=replace_blanks(word,guessed)       
            print("word:",new_word)
            print("wrong guesses:",wrong_guesses) 
               
       
            if new_word==word:
                print("####congratulation####! The word was :",word)
                break
            
        else:
            wrong_guesses.append(guess)
            count-=1
            print("wrong guesses:",wrong_guesses)
            print("Turns remaining:",count)   
            print("word:",replace_blanks(word,guessed))
        
       
           
            
if __name__=='__main__':
    main_function()
