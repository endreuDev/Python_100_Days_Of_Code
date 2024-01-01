import random
import hangman_art
import hangman_words

end_of_game = False
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

lives = 6

display = []
for _ in range(word_length):
    display += "_"

print(hangman_art.logo)

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was {chosen_word}!")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])
