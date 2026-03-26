import random
import os
import time

def clear_screen():
    # Clears the console screen for better UX
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(level, score):
    clear_screen()
    print("==================================================")
    print("           🎯 NUMBER GUESSING GAME 🎯           ")
    print("==================================================")
    print(f"| Level: {level:<13} | Score: {score:<14} |")
    print("==================================================")

def main():
    score = 0
    level = 1
    
    # Configuration for different levels: (Max Number, Attempts allowed, Points per remaining attempt)
    levels_config = {
        1: {"max_num": 10, "attempts": 4, "points_multiplier": 10},
        2: {"max_num": 50, "attempts": 6, "points_multiplier": 25},
        3: {"max_num": 100, "attempts": 8, "points_multiplier": 50},
        4: {"max_num": 500, "attempts": 10, "points_multiplier": 100},
        5: {"max_num": 1000, "attempts": 12, "points_multiplier": 200},
    }

    clear_screen()
    print("Welcome to the Ultimate Number Guessing Game!")
    print("Try to guess the hidden number to advance levels.")
    print("The fewer attempts you use, the more points you earn!\n")
    input("Press [Enter] to start your adventure...")

    while True:
        # Check if player has cleared all levels
        if level not in levels_config:
            print_header("WINNER!", score)
            print("\n🎉 CONGRATULATIONS! You have beaten all the levels! 🎉")
            print(f"Your Final Score is: {score}")
            break

        config = levels_config[level]
        target_number = random.randint(1, config["max_num"])
        attempts_left = config["attempts"]
        
        print_header(level, score)
        print(f"\n🤖 I am thinking of a number between 1 and {config['max_num']}.")
        print(f"⚡ You have {attempts_left} attempts to guess it.")

        won_level = False
        
        # Game loop for the current level
        while attempts_left > 0:
            try:
                guess = input(f"\n➤ Enter your guess ({attempts_left} attempts left): ")
                guess = int(guess)
            except ValueError:
                print("⚠️  Invalid input! Please enter a valid integer.")
                continue

            if guess < 1 or guess > config["max_num"]:
                print(f"⚠️  Out of bounds! Choose a number between 1 and {config['max_num']}.")
                continue

            attempts_left -= 1

            if guess == target_number:
                # Calculate points based on remaining attempts (+1 for current winning attempt)
                points_earned = (attempts_left + 1) * config["points_multiplier"]
                score += points_earned
                print(f"\n✅ CORRECT! You found the number {target_number}!")
                print(f"🌟 You earned {points_earned} points!")
                won_level = True
                break
            elif guess < target_number:
                print("📈 Too low! Try a higher number.")
            else:
                print("📉 Too high! Try a lower number.")

        if won_level:
            level += 1
            print("\nAdvancing to the next level...")
            time.sleep(2.5)
        else:
            print(f"\n❌ GAME OVER! You ran out of attempts.")
            print(f"💀 The correct number was: {target_number}")
            print(f"🏆 Your final score: {score}")
            
            retry = input("\nDo you want to play again? (y/n): ").lower()
            if retry == 'y':
                score = 0
                level = 1
            else:
                print("\nThanks for playing! Goodbye. 👋")
                break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGame terminated. Thanks for playing! 👋")
