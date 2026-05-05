from blackjack_game import Card, Deck, Hand

deck = Deck()
deck.shuffle()

hand = Hand()
hand.add_card(deck.deal())
hand.add_card(deck.deal())

print("Your hand is: ")

for card in hand.cards:
    print(" ", card)

print(f"Total: {hand.get_total()}")