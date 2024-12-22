import random
words = ["aback","abaft","abandoned","abashed","aberrant","abhorrent","abiding","abject","ablaze","able","abnormal","aboard","aboriginal","abortive","abounding","abrasive","abrupt","absent","absorbed","absorbing","abstracted","absurd","abundant","abusive","accept","acceptable","accessible","accidental","account","accurate","achiever","acid","acidic","acoustic","acoustics","acrid","act","action","activity","actor","actually","ad hoc","adamant","adaptable","add","addicted","addition","adhesive","adjoining","adjustment","admire","admit","adorable","adventurous","advertisement","advice","advise","afford","afraid","aftermath","afternoon","afterthought","aggressive","agonizing","agree","agreeable","agreement","ahead","air","airplane","airport","ajar","alarm","alcoholic","alert","alike","alive","alleged","allow","alluring","aloof","amazing","ambiguous","ambitious","amount","amuck","amuse","amused","amusement","amusing","analyze","ancient","anger","angle","angry","animal","animated","announce","annoy","annoyed","annoying","answer","ants","anxious","apathetic","apologise","apparatus","apparel","appear","applaud","appliance","appreciate","approval","approve","aquatic","arch","argue","argument","arithmetic","arm","army","aromatic","arrange","arrest","arrive","arrogant","art","ashamed","ask","aspiring","assorted","astonishing","attach","attack","attempt","attend","attract","attraction","attractive","aunt","auspicious","authority","automatic","available","average","avoid","awake","aware","awesome","awful","axiomatic"]
import string


def get_valid_word(words):
    word = random.choice(words) #randomly chooses a word from the list
    #Get the computer to interate over random words until there is a valid word without a - or a space
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()
def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)#import a string of all uppercase letters in the alphabet
    used_letters = set() #what the user has guessed

    lives = 7

    #getting user input
    while len(word_letters) > 0 and lives > 0: #iterate over this loop until the user has guessed all the letters or loses all their lives
        #we want to tell the user which letters they have used
        # " ".join(["a", "b", "cd"]) --> "a b cd"
        print("You have", lives, "lives left and have used these letters: "," ".join(used_letters))

        #we want to tell the user what the word is, but only reveal the letters they have guessed "W - R D"
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word is: ", " ".join(word_list))

        user_letter = input("Guess a letter: " ).upper() #user letter is the letter guessed by the user
        if user_letter in alphabet - used_letters: #if the user input is a letter and and hasnt been guessed run this block of code
            used_letters.add(user_letter) #this should add the user input to the list of used letters
            if user_letter in word_letters: #if the user input is in the word then run this block of code
                word_letters.remove(user_letter) #remove the correct user input from the list of the word letters
                print("")
            
            else: #the letter can only be right or wrong so else the letter is wrong and we want to subtract 1 life
                lives = lives - 1
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print ("\nYou already guessed that letter")

        else:
            print ("\nPlease guess a valid character")
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')

if __name__ == '__main__':
    hangman()


