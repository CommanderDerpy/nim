from nim import Nim


def start_game():
    play = input("Welcome to nim, would you like to play? (y/n)")

    while play.lower() == 'y':
        print("Lets play!")

        game = Nim()
        game.start()
        game.tell_winner()

        play = input("Would you like to play again? (y/n)")

    print("Thanks for playing!")


if __name__ == "__main__":
    start_game()
