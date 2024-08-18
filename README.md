# Rock, Paper, Scissors Game by Zehra Kezer

Welcome to the **Rock, Paper, Scissors** game, a timeless battle of wits and chance! This Python implementation brings the classic game to your terminal, allowing you to face off against a computer opponent. Will you master the strategy, or will luck decide your fate?

## Game Overview

In this game, you will challenge the computer to a series of Rock, Paper, Scissors duels. Each player selects one of three possible moves, and the winner is determined by simple but strategic rules. The first player (either you or the computer) to win two rounds wins the game.

## How to Play

1. **Start the Game**: Run the script in your terminal. The game will greet you with instructions and ask for your first move.
2. **Make Your Move**: Type "rock", "paper", or "scissors" when prompted. The computer will then randomly select its move.
3. **Win Rounds**: The winner of each round is determined by the following rules:
   - Rock crushes Scissors
   - Scissors cuts Paper
   - Paper covers Rock
4. **Score Tracking**: The game will keep track of your score and the computer's score. The first to reach two points wins the game.
5. **Continue or Exit**: After each game, you can choose to play again or exit the game.

## Game Strategy

While Rock, Paper, Scissors is often seen as a game of chance, there is room for strategy:
- **Predicting the Computer**: Over multiple rounds, you might notice patterns in the computer's choices. Try to anticipate its next move!
- **Mind Games**: The game is as much about psychology as it is about probability. Consider what the computer "expects" you to play and surprise it.
- **Random Play**: Alternatively, you can try to be as unpredictable as possible, just like the computer.

## Behind the Scenes: How It Works

The game is built using basic Python programming concepts, making it an excellent project for beginners to learn from:
- **Randomness**: The computer's move is determined using Python's `random.choice()` function, which selects a move at random from the possible options.
- **Conditional Logic**: The game uses a series of `if-elif-else` statements to determine the outcome of each round.
- **Loops**: A `while` loop ensures the game continues until a player decides to stop or the win condition is met.
- **User Input**: The game interacts with the player using Python's `input()` function, making it a fully interactive experience.

## Possible Extensions

This game is just the beginning! Here are some ideas for expanding and enhancing the game:
- **Multiplayer Mode**: Allow two players to play against each other on the same computer.
- **Score History**: Keep track of how many games the player has won or lost in a session.
- **AI Enhancement**: Implement a more advanced AI that learns from the player's choices and adapts its strategy.
- **Graphical Interface**: Convert the game into a GUI application using a library like Tkinter or Pygame.
- **Sound Effects**: Add sound effects to make the game more engaging.

## Example Game Session

Here’s what a typical game session might look like:

```shell
                Welcome to 'Rock, Paper, Scissors'!
This classic game is played between two players, with each player choosing between rock, paper or scissors.
The game is based on simple rules:
  1. Rock breaks scissors,
  2. paper covers rock,
  3. scissors cuts paper.
Your goal is to earn the most points playing against the computer. The first team to reach two points wins the game.
Enter rock, paper, or scissors to play, or if you do not want to play, write 'exit'
Let's start!

#### Game: 1 , Round: 1 ####

Rock, paper, scissors or exit:rock
Computer's move: rock

It's a tie this round!

Computer: 0 , Player:  0

########################################

#### Game: 1 , Round: 2 ####

Rock, paper, scissors or exit:rock
Computer's move: paper

Computer Won

Computer: 1 , Player:  0

########################################

#### Game: 1 , Round: 3 ####

Rock, paper, scissors or exit:rock
Computer's move: paper

Computer Won

Computer: 2 , Player:  0

########################################


Game Over!,The winner of this round is the Computer 
Player: 0, Computer: 2

Do you want to continue (yes/no): no

If you want to play again I'll be waiting here, bye for now
