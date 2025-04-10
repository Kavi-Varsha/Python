import random

def play():
    symbols = ['🍒', '🍇', '🍉', '7️⃣']  # Slot machine symbols
    while True:
        # Generate 3 random symbols
        results = random.choices(symbols, k=3)

        # Display the results in a formatted way
        print(" | ".join(results))

        # Check for jackpot
        if all(item == '7️⃣' for item in results):
            print("Jackpot! 💰")
        else:
            print("Thanks for playing!")

        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (Y or N): ").strip().upper()
        if play_again != 'Y':
            print("Goodbye! Thanks for playing!")
            break  # Exit the loop

play()
