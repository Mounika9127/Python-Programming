import random

# Predefined list of words
word_list = ["apple", "banana", "mango", "grape", "peach"]
secret_word = random.choice(word_list)

# Variables to track game state
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

# Display placeholder for the word
display_word = ["_" for _ in secret_word]

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")
print(f"You have {max_attempts} incorrect guesses allowed.\n")

while incorrect_guesses < max_attempts and "_" in display_word:
    print("Word:", " ".join(display_word))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❌ Please enter a single alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Good guess!\n")
        for index, letter in enumerate(secret_word):
            if letter == guess:
                display_word[index] = guess
    else:
        incorrect_guesses += 1
        print(f"❌ Wrong guess! {max_attempts - incorrect_guesses} attempts left.\n")

# Final result
if "_" not in display_word:
    print("🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("💀 Game Over! The word was:", secret_word)
