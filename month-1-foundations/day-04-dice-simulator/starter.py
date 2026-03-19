# Day 4: Dice Game Simulator
# A casino dice game using random, sys, statistics, and rich.

import random
import sys

# TODO: pip install rich cowsay
# from rich.console import Console
# import cowsay

# console = Console()


def roll_dice():
    """Roll two dice and return their values and sum."""
    # TODO: Use random.randint(1, 6) for each die
    # TODO: Return (die1, die2, total)
    pass


def display_roll(die1, die2, total):
    """Display the dice roll in a fun way."""
    # TODO: Print the roll (use rich colors or ASCII art)
    pass


def play_round(balance, bet):
    """Play one round of craps. Returns the new balance."""
    # TODO: First roll
    # TODO: If 7 or 11: win
    # TODO: If 2, 3, or 12: lose
    # TODO: Otherwise: set point, keep rolling
    pass


def get_bet(balance):
    """Ask the player for their bet amount."""
    # TODO: Get input
    # TODO: Validate (must be positive, can't exceed balance)
    # TODO: Handle bad input
    pass


def show_statistics(rolls, wins, losses):
    """Show game statistics at the end."""
    # TODO: Use statistics module for mean, mode
    # TODO: Show total games, win rate, biggest streak
    pass


def main():
    """Main game loop."""
    # TODO: Parse sys.argv for starting balance
    balance = 100
    if len(sys.argv) > 1:
        pass  # TODO: Parse starting balance from args

    rolls = []
    wins = 0
    losses = 0

    print("=== Welcome to Dice Game! ===")
    print(f"Starting balance: ${balance}\n")

    # TODO: Game loop (play until broke or quit)
    # TODO: Show statistics at the end


if __name__ == "__main__":
    main()
