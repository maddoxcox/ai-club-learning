# Day 4: Dice Game Simulator

## What You're Building
A casino-style dice game (Craps simplified). The player bets fake money, rolls dice, and tries to win. Uses multiple Python standard library modules and a fun third-party package.

## What You'll Learn
- `random` module — generating random numbers
- `sys` module — command-line arguments (`sys.argv`)
- `statistics` module — calculating odds and averages
- Third-party packages — `cowsay` or `rich` for fun output
- Command-line arguments — running scripts with options

## Setup
```
pip install cowsay rich
```

## Requirements
Build `dice_game.py` that:

1. **Game setup:**
   - Player starts with $100 (or custom amount via `sys.argv`)
   - Each round, they choose how much to bet

2. **Game mechanics (simplified Craps):**
   - Roll two dice
   - If roll is 7 or 11: WIN (double your bet)
   - If roll is 2, 3, or 12: LOSE (lose your bet)
   - Any other number: that becomes your "point" — keep rolling until you hit your point (win) or roll a 7 (lose)

3. **Display:**
   - Show dice rolls with ASCII art or emoji
   - Use `rich` for colored output (green for wins, red for losses)
   - Use `cowsay` for game messages (optional, for fun)
   - Show running balance

4. **Statistics tracking:**
   - Track all rolls in a list
   - At the end, show: total games, wins, losses, biggest win, average roll (use `statistics.mean`)

5. **Command-line options:**
   - `python dice_game.py` — start with $100
   - `python dice_game.py 500` — start with $500
   - `python dice_game.py 500 --auto 20` — auto-play 20 rounds (stretch)

## How to Work
- Start with basic dice rolling (random.randint)
- Add the game logic
- Add betting
- Add pretty output with rich/cowsay
- Add statistics at the end

## Stretch Goals
- Add an auto-play mode that simulates 1000 games and shows the house edge
- Add a high score file (saves to JSON)
- Add different game modes (high-low, over-under)

## When You're Done
```
git add .
git commit -m "Day 4: Dice Game with random, sys, statistics, and rich"
git push
```
