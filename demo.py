from group_13_final.blackjack_game import Card, Deck, Hand
#import card, deck, and hand classes from main code

deck = Deck()
#create a deck object (new deck)
deck.shuffle()
#randomly shuffle the deck


hand = Hand()
#create new hand object (empty hand)
hand.add_card(deck.deal())
hand.add_card(deck.deal())
#takes top card off deck and adds it to hand (twice for two cards per hand)

print("Your hand is: ")


for card in hand.cards:
    print(" ", card)
#loops through each card in hand
#prints calling card.__str__() 

print(f"Total: {hand.get_total()}")
#print total using get_total() which adds up the cards int values