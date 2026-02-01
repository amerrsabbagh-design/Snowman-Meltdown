from game_logic import play_game


def ask_replay():
    while True:
        choice = input("Play again? (y/n): ").strip().lower()
        if choice in ("y", "n"):
            return choice == "y"
        print("Please type 'y' or 'n'.")


if __name__ == "__main__":
    while True:
        play_game()
        if not ask_replay():  # standard replay pattern [web:13][web:22]
            print("Thanks for playing!")
            break