import random
class Card:
    """
    Representing a singple playing card
    
    args:
        suit(str): the suit of the card: Hearts, Diamonds, Spades, Or clubs.
        rank(str): Thr rank of the card, such as 2-10, Jack, Queen, King, or Ace
        
    Author: Goldheim & Wazhuddin    
    """  
class Deck:
    """
    Represents a standard deck of 52 playing cards
    
    Author: Goldheim & Wazihuddin
    """
    
    def shuffle(self):
        """
        Shuffle the deck in a random order
        
        Author: Wazihuddin
        
        """
        random.shuffle(self.cards)
        
    def deal(self):
        pass
    pass

class Hand:
    """
    Represents the cards currently held by a player or dealer
    
    Author: Wazihuddin
    
    """
    def __init__(self):
        self.cards = []
        self.total = 0
    
    def add_card(self, card):
        """Adds a card to the hand
        
        args:  the card to add
        
        author: Wazihuddin
        
        """
    def get_total(self):
        """
        Calculate the total value of the hand, making sure ace is adjusted from 11 to 1 as needed
        
        Returns: int: The best blackjack total for the hand.
        
        Author: Stanton
        
        """
        aces = 0
        
        for card in self.cards:
            self.total += card.value
        # needs aces count pending on names used in card class 
        while self.total > 21 and aces > 0:
            self.total -= 10
            aces -= 1
            
        return self.total
    
    def get_power_suit(self):
        """
        The suit of the first card
        
        Returns(str): The first card's suit, or none if hand is empty
        
        Author: Wazihuddin
        """
        if len(self.cards) > 0:
            return self.cards[0].suit
        return None
    
    def __str__():
        pass

class Player:
    """
    Stores the player's name, chips, hand, and next-round stats
    
    args:
    name(Str): the players name
    chips(int): starting number of chips
    
    Author: Isha
    """
    def __init__(self, name: str, chips: int):
        self.name = name
        self.chips = chips
        self.hand = []
        self.next_round_stats = {}
        """
        test
        1
        2
        3
        """
    def place_bet():
        """
        deducts from the players chip balance, applying any club discount
        
        args: amount(float): the intended amount to bet
        
        returns(float): the final amount deducted from the players chips
        
        author: 
        """
    def add_winnings():
        """
        Adds chips to the players balance after a round
        
        args: amount(float): the number of chips to add
        
        author: 
        """
class Bet:
    """
    Store the current rounds wager and determind payout outcomes.
    
    args: amount(float): the amount wagered this round
    
    author: 
    """
    def __init__():
        pass
    
    def resolve_outcome():
        """
        Compute the round payout using blackjack rules and first-card suit power
        
        Orignal algorithm steps:
        1. get the players total and dealers total
        2. check if the player busted
        3. check if the dealer busted or if the player won
        4. check if the result is a push.
        5. apply the first-card suit power-up
        6. return the final payout
        
        args: player_hand & dealer_hand
        
        author: 
        """
        
        pass

def blackjack_check():
    """
    check weather a hand is a blackjack
    
    args: hand: evaluating the hand
    
    Returns: bool: true if the hand has two cards that add up to 21, false otherwise
    
    author: Stanton
    """
    total = Hand.get_total()
    
    return True if total == 21 and len(Hand.cards) == 2 else False

def player_turn():
    """
    player turn
    
    args:
        player: the player taking the turn
        deck: the current deck
        
    author:
    """
    
    pass
def dealer_turn():
    """
    run the dealers turn
    
    args:
        dealer: the dealer
        deck: the currnt deck
        
    author:
    """
    pass                

def apply_club_discount():
    """apply the clubs power-up if the players first card is a club
    
    args: player: the player recives a discount
    
    author:
    
    """
    pass

def reveal_hidden_card_spade():
    """
    reveal dealers hidden card if the players first card is a spade
    
    args:
        player: the player
        dealer: the dealer
        
    author:
    """
    
    pass

def main():
    pass