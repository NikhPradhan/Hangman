import random

def play(word):
    word_length=["-"]*len(word)
    attempt=6
    guessed_letters=[]
    print(word_length)
    print("your number of attempts",attempt)
    hangman(attempt)
##Loop until attempt runs out or successfully guesses all the letters
    while attempt > 0:
        guess=input("Guess a letter:\n").lower()
        
        if guess in guessed_letters:
            print(word_length)
            print("You already guessed this letter")
            hangman(attempt)
        elif guess in word:
            guessed_letters.append(guess)
            for i in range(0,len(word)):
                if guess == word[i]:
                    word_length[i]=guess
            print(word_length)
            print("Good guess\n")
            hangman(attempt)
            if "-" in word_length:
                continue
            else:
                break
        else:
            print("You guessed it wrong")
            guessed_letters.append(guess)
            attempt-=1
            print(word_length)
            print("your number of attempts",attempt)
            hangman(attempt)
            
    if attempt > 0:
        print("You successfully guessed the word ")
    else:
        print("you ran out of attepts")

#### Function for printing hangman at every guess
        
def hangman(attempt):
    stages=[ """
        -----------
        |         |
        |         O       Your man is hanged !!!
        |        /|\\
        |         |
        |        / \\
        |
      """,
      """
        -----------
        |         |
        |         O 
        |        /|\\
        |         |
        |        /
        |
      """, 
      
      """
        -----------
        |         |
        |         O 
        |        /|\\
        |         |
        |
        |
      """,
      """
        -----------
        |         |
        |         O 
        |        /|
        |         |
        |
        |
      """,
      """
        -----------
        |         |
        |         O 
        |         |
        |         |
        |
        |
      """,
      """
        -----------
        |         |
        |         O 
        |
        |
        |
        |
      """,
      """
        -----------
        |
        | 
        |
        |
        |
        |
        """]
    print(stages[attempt])

#######


flag='Y'
while flag == 'Y':
    word_list=["apple","ball","cat","nikhil"]
    word=random.choice(word_list)
    play(word)
    flag=input("Do you want to play again? Y/N\n").upper()

            
            
        
        
    
    
    
