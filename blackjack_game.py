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
    
    def add_card(self, card):
        """Adds a card to the hand
        
        args: the card to add
        
        author: Wazihuddin
        
        """
    def get_total(self):
        """
        Calculate the total value of the hand, making sure ace is adjusted from 11 to 1 as needed
        
        Returns: int: The best blackjack total for the han.
        
        Author:
        
        """
class Player:
    """
    Stores the player's name, chips, hand, and next-round stats
    
    args:
    name(Str): the players name
    chips(int): starting number of chips
    
    Author:
    """
    def __init__():
        pass
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
        pass

def blackjack_check():
    pass

def dealer_turn():
    pass                

def apply_club_discount():
    pass

def reveal_hidden_card_spade():
    pass

def main():
    pass