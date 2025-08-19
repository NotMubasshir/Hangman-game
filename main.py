import random

# List of words for the game
words = ["python", "hangman", "computer", "science", "programming", "challenge"]

# Pick a random word
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6  # Number of chances

print("🎮 Welcome to Hangman!")
print("Guess the word:")

# Game loop
while attempts > 0 and "_" in guessed:
    print("\n" + " ".join(guessed))
    print(f"Attempts left: {attempts}")

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single letter.")
        continue

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
        print("✅ Correct!")
    else:
        attempts -= 1
        print("❌ Wrong!")

# Win or lose
if "_" not in guessed:
    print("\n🎉 You win! The word was:", word)
else:
    print("\n💀 You lost! The word was:", word)
