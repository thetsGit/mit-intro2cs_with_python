# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed = False
    valid_letters = list(secret_word)
    for letter in letters_guessed:
        while letter in valid_letters:
            valid_letters.remove(letter)
    if len(valid_letters) == 0:
        guessed = True
    return guessed



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_list = ['_ ' for word in secret_word]
    secret_word_list = list(secret_word)
    for letter in letters_guessed:
        while letter in secret_word_list:
             guessed_list[secret_word_list.index(letter)] = letter
             secret_word_list[secret_word_list.index(letter)] = '_ '
    return ''.join(guessed_list)



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    available_letters = list(string.ascii_lowercase)
    for letter in list(letters_guessed):
        while letter in available_letters:
            available_letters.remove(letter)
    return ''.join(available_letters)
    
    
def get_unique_letters_count(secret_word):
    unique_letters_list=[]
    unique_letters_count=0
    for char in secret_word:
      if ((char in unique_letters_list) == False):
        unique_letters_list.append(char)
        unique_letters_count += 1
    return unique_letters_count

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed = []
    remaining_guessing_chance = 6
    warning = 3
    vowels = ['a','e','i','o','u']
    print('Welcome to the game Hangman!\n')
    print('I am thinking of a word that is',len(secret_word),'long\n--------------------')
    while (True):
        print('You have',remaining_guessing_chance,'guessed left.')
        print('Available letters :', get_available_letters(letters_guessed))

        #input request and validation
        user_input = (input('Please guess a letter: ')).lower()

        #check if alphabet
        if (user_input.isalpha() == False):
          if(warning > 0):
           warning -= 1
           print('Oops! That is not a valid letter. You have',warning,'warnings left:',get_guessed_word(secret_word,letters_guessed))
           if warning == 0:
             print('WARNING!!! remember you have 0 warning left, your guessing chances will be reduced as a penalty from now.')
          else:
           remaining_guessing_chance -= 1
           print('Oops! That is not a valid letter. You now have',remaining_guessing_chance,'guesses left:',get_guessed_word(secret_word,letters_guessed))

        #catch repeated guess
        elif user_input in letters_guessed:
          if(warning > 0):
           warning -= 1
           print('Oops! You\'ve already guessed that letter. You now have',warning,'warnings left:',get_guessed_word(secret_word,letters_guessed))
           if warning == 0:
             print('WARNING!!! remember you have 0 warning left, your guessing chances will be reduced as a penalty from now.')
          else:
           remaining_guessing_chance -= 1
           print('Oops! You\'ve already guessed that letter. You now have',remaining_guessing_chance,'guesses left:',get_guessed_word(secret_word,letters_guessed))
  
        #good guess check
        elif user_input in secret_word:
          letters_guessed.append(user_input)
          print('Good guess:',get_guessed_word(secret_word,letters_guessed))

        #bad guess check
        else:
          letters_guessed.append(user_input)
          print('Oops! That letter is not in my word:',get_guessed_word(secret_word,letters_guessed))
          if user_input in vowels:
            remaining_guessing_chance -= 2
          else: 
            remaining_guessing_chance -= 1
        if((remaining_guessing_chance <= 0) or (is_word_guessed(secret_word,letters_guessed) == True)):
          break
        print('\n___________________________\n')
    
    if (is_word_guessed(secret_word,letters_guessed) == True):
       print('Congratulations, you have won!\nYour total score for this game is:',get_unique_letters_count(secret_word)*remaining_guessing_chance)
    else:
       print('U have lost! My word is',secret_word)



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass
    
    result = True
    for i in range(len(my_word)):
      if (my_word[i] != '_'):
        if (my_word[i] != other_word[i]):
            result = False
      else:
        if other_word[i] in my_word:
            result = False
      if (result == False): break
    return result

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass
    same_length_words = []
    match_words = []
    my_word = my_word.replace(' ','')
    for word in wordlist:
      if (len(word) == len(my_word)): same_length_words.append(word)
    for other_word in same_length_words:
      if (match_with_gaps(my_word,other_word) == True): match_words.append(other_word)
    return ' '.join(match_words) if len(match_words) != 0 else 'No Matches Found'


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed = []
    remaining_guessing_chance = 6
    warning = 3
    vowels = ['a','e','i','o','u']
    print('Welcome to the game Hangman!\n')
    print('I am thinking of a word that is',len(secret_word),'long\n___________________________\n')
    while (True):
        print('You have',remaining_guessing_chance,'guessed left.')
        print('Available letters :', get_available_letters(letters_guessed))

        #input request and validation
        user_input = (input('Please guess a letter: ')).lower()

        #check if alphabet
        if (user_input == '*'):
          if (len(letters_guessed)<3): print('You have to guess two times at least to unlock this feature, guess a bit more and try it later.')

          else: print('Possible word matches are:\n',show_possible_matches(get_guessed_word(secret_word,letters_guessed)),'\n___________________________\n')
          continue

        if (user_input.isalpha() == False):
          if(warning > 0):
           warning -= 1
           print('Oops! That is not a valid letter. You have',warning,'warnings left:',get_guessed_word(secret_word,letters_guessed))
           if warning == 0:
             print('WARNING!!! remember you have 0 warning left, your guessing chances will be reduced as a penalty from now.')
          else:
           remaining_guessing_chance -= 1
           print('Oops! That is not a valid letter. You now have',remaining_guessing_chance,'guesses left:',get_guessed_word(secret_word,letters_guessed))

        #catch repeated guess
        elif user_input in letters_guessed:
          if(warning > 0):
           warning -= 1
           print('Oops! You\'ve already guessed that letter. You now have',warning,'warnings left:',get_guessed_word(secret_word,letters_guessed))
           if warning == 0:
             print('WARNING!!! remember you have 0 warning left, your guessing chances will be reduced as a penalty from now.')
          else:
           remaining_guessing_chance -= 1
           print('Oops! You\'ve already guessed that letter. You now have',remaining_guessing_chance,'guesses left:',get_guessed_word(secret_word,letters_guessed))
  
        #good guess check
        elif user_input in secret_word:
          letters_guessed.append(user_input)
          print('Good guess:',get_guessed_word(secret_word,letters_guessed))

        #bad guess check
        else:
          letters_guessed.append(user_input)
          print('Oops! That letter is not in my word:',get_guessed_word(secret_word,letters_guessed))
          if user_input in vowels:
            remaining_guessing_chance -= 2
          else: 
            remaining_guessing_chance -= 1
        if((remaining_guessing_chance <= 0) or (is_word_guessed(secret_word,letters_guessed) == True)):
          break
        print('\n___________________________\n')
    
    if (is_word_guessed(secret_word,letters_guessed) == True):
       print('Congratulations, you have won!\nYour total score for this game is:',get_unique_letters_count(secret_word)*remaining_guessing_chance)
    else:
       print('U have lost! My word is',secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
