import random # We import the random module so that the computer can make random moves

def rock_paper_scissors_Zehra_Kezer():

    # The part that gives information and instructions to the player when the game starts
    print("                \033[1mWelcome to 'Rock, Paper, Scissors'!\033[0m"
        "\nThis classic game is played between two players, with each player choosing between rock, paper or scissors. ",
        "\nThe game is based on simple rules: "
        "\n  1. Rock breaks scissors, "
        "\n  2. paper covers rock, "
        "\n  3. scissors cuts paper. "
        "\nYour goal is to earn the most points playing against the computer. The first team to reach \033[1mtwo\033[0m points wins the game."
        "\nEnter rock, paper, or scissors to play, or if you do not want to play, write 'exit'"
        "\nLet's start!\n")

    # We define a counter to keep track of the number of games
    game_counter=0

    while True: # The game can be replayed in an infinite loop

        # Scores and round counts are reset every time a game starts
        player_counter=0
        computer_counter=0
        round_counter=1
        game_counter+=1  # We are increasing the number of games by one


        # Moves that the computer can make
        moves = ["rock","paper","scissors"]



        # We check the scores of the computer and the player while the game is in progress. If anyone's score reaches 2, the game is over and the winner is clear.
        while computer_counter<2 and player_counter<2:

            print("#### Game:" , game_counter,", Round:",round_counter,"####\n")

            computer =random.choice(moves) # The computer chooses a random move

            # Getting the player's move
            player = input('Rock, paper, scissors or exit:').lower()

            # Evaluating the winner of the round based on the moves
            if player== "rock" and computer=="scissors":
                player_counter+=1
                print("Computer's move:", computer)
                print("\nPlayer Won\n")
            elif player== "rock" and computer=="paper":
                computer_counter+=1
                print("Computer's move:", computer)
                print("\nComputer Won\n")
            elif player== "scissors" and computer=="rock":
                computer_counter+=1
                print("Computer's move:", computer)
                print("\nComputer Won\n")
            elif player=="scissors" and computer=="paper":
                player_counter+=1
                print("Computer's move:", computer)
                print("\nPlayer Won\n")
            elif player== "paper" and computer=="scissors":
                player_counter+=1
                print("Computer's move:", computer)
                print("\nPlayer Won\n")
            elif player== "paper" and computer=="rock":
                computer_counter+=1
                print("Computer's move:", computer)
                print("\nComputer Won\n")
            elif player == computer:
                print("Computer's move:", computer)
                print("\nIt's a tie this round!\n")
            elif player== "exit":
                # If the player wants to exit the game by typing 'exit', the program ends.
                # If it comes out of the first game it will say something different after a game is completed
                if game_counter==1:
                    print("\nIt's sad. I'm sure I could beat you.But if you want to play I'm here.\n")
                    break
                else:
                    print("Thanks for playing!")
                    break
            else:
                # Gives an error message to the user when there is invalid input
                print("\nInvalid choice\n")

            # We print the scores on the screen
            print("Computer:",computer_counter,",", "Player: ",player_counter)
            print("\n########################################\n")

            # We increase the number of rounds by one
            round_counter+=1

        # If the player wants to exit the game, the player can exit the game by typing exit.
        if player== "exit":
            break

        # We determine the winner according to the result of the game
        if computer_counter > player_counter:
            print(f"\nGame Over!,The winner of this round is the \033[1mComputer\033[0m \nPlayer: {player_counter}, Computer: {computer_counter}")
        else:
            print(f"\nCongratulations!,The winner of this round is the \033[1mPlayer\033[0m \nPlayer: {player_counter}, Computer: {computer_counter}")




        # Asks the player if he/she wants to continue to the next game
        challenge = ""

        while challenge !="yes" or challenge!="no":
            challenge = input('\nDo you want to continue (yes/no): ').lower()

            if challenge== "yes":
                break
            elif challenge=="no":
                print("\nIf you want to play again I'll be waiting here, bye for now")
                break
            else:
                # Gives an error message to the user when there is invalid input
                print("invalid choice")

        if challenge== "no":
                    break

        #Does the computer want to play games?
        option = ["yes","no"]
        computer_choice =random.choice(option)

        if computer_choice=="yes":
            print("\nI want to play again as well! Let's play one more!")
        else:
            print("\nI'm sorry but I don't want to play :) ")
            break



rock_paper_scissors_Zehra_Kezer()