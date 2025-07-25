import random
import hangman_art
import hangman_words
lives = 6
choice_word = random.choice(hangman_words.word_list)
print (hangman_art.logo)
display = ["_" for _ in choice_word]
print(display)

end_of_the_game = False

while not end_of_the_game:
    guess = input("Put a letter: ").lower()

    if guess in display:
        print("You already guessed that letter.")

    for position in range(len(choice_word)):
        letter = choice_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in choice_word:
        lives -= 1
        print(f"Wrong guess. You lost a life. Lives left: {lives}")
        if lives == 0:
            end_of_the_game = True
            print("You Lose!")
            print(f"The word was: {choice_word}")

    print(display)
    print(hangman_art.stages)

    if "_" not in display:
        end_of_the_game = True
        print("You Win!")
