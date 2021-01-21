import random
from words import word_list


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return stages[tries]


def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    guessed = False
    guessed_letters = []
    guessed_words = []
    triesLeft = 6
    word_completed = '_ ' * len(word)
    print(word_completed)
    print('\n')

    while not guessed and triesLeft > 0:
        guess = input("Take a guess: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in word:
                print(guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completed)
                indices = [i for i, letter in enumerate(
                    word) if letter == guess]
                for index in indices:
                    word_as_list[index * 2] = guess

                word_completed = "".join(word_as_list)
                if '_' not in word_completed:
                    guessed = True
                print(word_completed)

            elif guess in guessed_letters:
                print('You have already guessed', guess)
            else:
                print("Wrong letter")
                triesLeft -= 1
                print('You have ', triesLeft, 'tries left')
                guessed_letters.append(guess)

        elif len(guess) == len(word) and guess.isalpha():
            if guess == word:
                print("You Got It!")
                guessed = True
                word_completed = word

            elif guess in guessed_words:
                print('You have already guessed', guess)
            else:
                print('Incorrect guess')
                guessed_words.append(guess)
                triesLeft -= 1
                print('You have', triesLeft, 'tries left')

        else:
            print('Invalid guess')

        print(display_hangman(triesLeft))
        print(word_completed)
        print('\n')

    if guessed:
        print("Congrats on guessing the word!")

    if triesLeft == 0:
        print("Better luck next time. The word is", word)


def main():
    play(get_word())
    while input("Do you want to play again? (Y/N) ").upper() == 'Y':
        play(get_word())


main()

# if __name__ == '__main__':
#     main()
