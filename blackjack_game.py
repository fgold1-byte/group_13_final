import random
import pandas

suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]

starting_chips = 100



class Card:
    
    face_cards = ["Jack", "Queen", "King", "Ace"]
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    
    
    def card_value(self):
        rank_values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}
        
        return rank_values[self.rank]
        
    def __str__(self):
        return (f"{self.rank} of {self.suit}")
        
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
    def __init__(self):
        self.cards = [Card (suit, rank) for suit in suits for rank in ranks]
        
    
    def shuffle(self):
        """
        Shuffle the deck in a random order
        
        Author: Wazihuddin
        
        """
        random.shuffle(self.cards)
        
    def deal(self):
        """
        Deal top card from deck, raise error if cards are out
        
        Returns:
            top card
        Raises:
            ValueError(str)
            
        Author: Goldheim
        """
        if not self.cards:
            raise ValueError("Out of cards, start new game")
        return self.cards.pop()
    
    

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
        self.cards.append(card)
    def get_total(self):
        """
        Calculate the total value of the hand, making sure ace is adjusted from 11 to 1 as needed
        
        Returns: int: The best blackjack total for the hand.
        
        Author: Stanton
        
        """
        aces = 0
        
        for card in self.cards:
            self.total += card.card_value()
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

class Player(Hand):
    """
    Stores the player's name, chips, hand, and next-round stats, subclass of Hand
    
    args:
    name(Str): the players name
    chips(int): starting number of chips
    
    Author: Isha and Goldheim
    """
    def __init__(self, name: str, chips: int):
        super().__init__()
        self.name = name
        self.chips = chips
        self.next_round_stats = {}
        """
        test
        1
        2
        3
        """
    def place_bet(self, amount: float):
        """
        deducts from the players chip balance, applying any club discount
        
        args: amount(float): the intended amount to bet
        
        returns(float): the final amount deducted from the players chips
        
        author: Goldheim
        """
        if amount > self.chips:
            raise ValueError(f"Not enough chips. You have {self.chips} left.")
        
        if self.get_power_suit() == "Clubs":
            amount = amount * 0.75
            print ("Club rule: Next bet is 25% off")
            
        self.chips == amount
        return amount
    
    
    def add_winnings():
        """
        Adds chips to the players balance after a round
        
        args: amount(float): the number of chips to add
        
        author: 
        """
        
    def pandas_graph():
        s = pd.series()
class Bet:
    """
    Store the current rounds wager and determind payout outcomes.
    
    args: amount(float): the amount wagered this round
    
    author: Wazihuddin
    """
    def __init__(self, amount):
        self.amount = amount
        self.result_status = "pending"
        self.payout = 0
    
    def resolve_outcome(self, player_hand, dealer_hand):
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
        
        author: Wazihuddin
        """
        
        player_total = player_hand.get_total()
        dealer_total = dealer_hand.get_total()
        power_suit = player_hand.get_power_suit()
        
        #If player bust
        if player_total > 21:
            self.result_status = "Loss"
            print(f"You busted with {player_total}! 💥")
            self.payout = 0
            
            if power_suit == "Hearts":
                self.payout = self.amount * 0.25
                print(f"Hearts power! You get back ${self.payout:.2f}")
                
                
        #if player wins
        elif dealer_total > 21 or player_total > dealer_total:
            self.result_status = "Win"
            self.payout = self.amount * 2
            print(f"You win! 🎉 Your total: {player_total} vs Dealer: {dealer_total}")
            
            if power_suit == "Diamonds":
                self.payout = self.amount * 3
                print(f"Diamonds power! Your payout is boosted to ${self.payout:.2f}")
                
        #push
        elif player_total == dealer_total:
            self.result_status = "Push"
            self.payout = self.amount
            print(f"Push! 🤝 You and the dealer both have {player_total}. Your bet is returned.")
            
        #player loses
        else:
            self.result_status = "Loss"
            self.payout = 0
            print(f"You lose. 😞 Your total: {player_total} vs Dealer: {dealer_total}")
            
            if power_suit == "Hearts":
                self.payout = self.amount * 0.25
                print(f"Hearts power! You get back ${self.payout:.2f}")
                
        return self.payout
        
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