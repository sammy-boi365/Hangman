import random
from jsonlist import words
import string


difficulty = input("Select your difficulty: [e]asy, [m]edium, [h]ard. If you do not enter in a valid difficulty, your difficulty will be defaulted to medium: ").lower()



def get_valid_word(select_word):
    word = random.choice(select_word)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    used_letters = set()  # what the user has guessed
    length = len(word_letters)
    count = 0
    alphabet = set(string.ascii_uppercase)


    while length >= 0:
        print("You have used these letters: ", ''.join(used_letters))
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))
        if len(word_letters) > 0:
            user_letter = input("Guess a letter: ").upper()
        else:
            print(f"Congratulations, you have guessed the correct word, {word}")
            break
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in word_letters:
            print("You have already used that letter. Try another letter.")
        elif user_letter not in alphabet:
            print("Invalid character")
        else:
            print("You have already guessed that letter.")
        count += 1
        if difficulty == "e":
            turns = length + round(length * .75) - count
        elif difficulty == "m":
            turns = length + round(length * .55) - count
        elif difficulty == "h":
            turns = length + round(length * .30) - count
        else:
            turns = length + round(length * .55) - count
        print(f"You have {turns} turn(s) left.")
        if turns == 0:
            if user_letter in word and length == 0:
                print(f"Congratulations, you have guessed the correct word, {word}")
            else:
                print(f"Aw, it looks like you've run out of turns. The correct word was {word}")
                break


hangman()