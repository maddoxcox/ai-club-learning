# Day 10: Blackjack
# A full card game built with object-oriented programming.


class Card:
    """Represents a single playing card."""

    SUITS = ["♥", "♦", "♣", "♠"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, suit, rank):
        # TODO: Store suit and rank
        pass

    @property
    def value(self):
        """Return the point value of this card."""
        # TODO: Number cards = face value, J/Q/K = 10, A = 11
        pass

    def __str__(self):
        # TODO: Return like "A♠" or "10♥"
        pass

    def __repr__(self):
        return self.__str__()


class Deck:
    """Represents a deck of 52 cards."""

    def __init__(self):
        # TODO: Create all 52 cards
        # TODO: Shuffle the deck
        pass

    def deal(self):
        """Deal one card from the deck."""
        # TODO: Remove and return the top card
        pass

    def __len__(self):
        # TODO: Return number of remaining cards
        pass


class Hand:
    """Represents a hand of cards."""

    def __init__(self):
        self.cards = []

    def add_card(self, card):
        """Add a card to the hand."""
        # TODO
        pass

    @property
    def total(self):
        """Calculate total value, handling Aces smartly."""
        # TODO: Sum all card values
        # TODO: If total > 21 and there are Aces, count some as 1 instead of 11
        pass

    @property
    def is_bust(self):
        """Check if hand is over 21."""
        # TODO
        pass

    @property
    def is_blackjack(self):
        """Check for blackjack (21 with exactly 2 cards)."""
        # TODO
        pass

    def __str__(self):
        # TODO: Show all cards and total
        pass


class Player:
    """Represents a player in the game."""

    def __init__(self, name, chips=100):
        # TODO: Store name, chips, hand, current bet
        pass

    def place_bet(self, amount):
        """Place a bet."""
        # TODO: Validate bet amount
        pass

    def hit(self, card):
        """Add a card to player's hand."""
        # TODO
        pass

    def win(self):
        """Player wins — double their bet."""
        # TODO
        pass

    def lose(self):
        """Player loses their bet."""
        # TODO
        pass


class Dealer(Player):
    """Represents the dealer. Inherits from Player."""

    def __init__(self):
        super().__init__("Dealer", chips=float("inf"))

    def should_hit(self):
        """Dealer must hit on 16 or less, stand on 17+."""
        # TODO
        pass

    def show_partial(self):
        """Show only the first card (other is hidden)."""
        # TODO
        pass


class Game:
    """Manages the Blackjack game."""

    def __init__(self):
        # TODO: Create player, dealer, deck
        pass

    def play_round(self):
        """Play one round of Blackjack."""
        # TODO: Get bet
        # TODO: Deal initial cards (2 each)
        # TODO: Check for blackjack
        # TODO: Player turn (hit/stand loop)
        # TODO: Dealer turn
        # TODO: Determine winner
        # TODO: Settle bets
        pass

    def play(self):
        """Main game loop."""
        # TODO: Loop rounds until player quits or is broke
        pass


if __name__ == "__main__":
    game = Game()
    game.play()
