# Day 10: Card Game (Blackjack)

## What You're Building
A full Blackjack game using object-oriented programming. Cards, Decks, Hands, and Players are all classes. The game loop handles hit/stand logic with proper OOP design.

## What You'll Learn
- Classes and `__init__` — creating objects
- `self` — instance methods and attributes
- Properties and `@property` decorator
- Inheritance — Player and Dealer share a base class
- `__str__` and `__repr__` — string representations
- Operator overloading — comparing hands

## Requirements
Build `blackjack.py` with these classes:

### Card Class
- Attributes: suit (Hearts, Diamonds, Clubs, Spades), rank (2-10, J, Q, K, A)
- Property: `value` — number cards = face value, J/Q/K = 10, A = 11 (or 1)
- `__str__`: displays like "A♠" or "10♥"

### Deck Class
- Contains 52 Card objects
- Methods: `shuffle()`, `deal()` (returns one card)
- `__len__`: returns remaining cards

### Hand Class
- Contains a list of Cards
- Property: `total` — sum of card values (handles Ace = 11 or 1)
- Property: `is_bust` — total > 21
- Property: `is_blackjack` — total == 21 with 2 cards
- `__str__`: shows all cards and total

### Player (inherits from a base class)
- Has a Hand, a name, and chips (money)
- Methods: `hit(card)`, `stand()`, `bet(amount)`

### Dealer (inherits from same base class)
- Same as Player but with dealer logic: must hit on 16, stand on 17
- First card is hidden until reveal

### Game Class
- Manages the game loop: deal, player turn, dealer turn, settle bets
- Handles all the game rules

## How to Work
- Build Card first, test it
- Build Deck, test it
- Build Hand with the tricky Ace logic
- Build Player and Dealer
- Build the Game loop last

## Stretch Goals
- Add multiple players
- Add card counting practice mode
- Add ASCII art for cards
- Save game statistics to JSON

## When You're Done
```
git add .
git commit -m "Day 10: Blackjack with OOP - classes, inheritance, properties"
git push
```
