from dataclasses import *
import random


@dataclass
class Card:
    suit: str
    rank: int


def new_stock():
    stock = []
    for suit in ["spade", "heart", "diamond", "club"]:
        for rank in range(1, 14):
            card = Card(suit, rank)
            stock.append(card)
    random.shuffle(stock)
    return stock


def new_hand(stock):
    cards = []
    for x in range(5):
        card = stock.pop()
        cards.append(card)
        print(cards)
    return cards


def change_heart(hand):
    for card in hand:
        card.suit = "heart"


def take_cards(stock, n):
    cards = []
    for x in range(n):
        card = stock.pop()
        cards.append(card)
    return cards


def print_card(card):
    print(f"{card.suit}の{card.rank}")


def is_flush(hand):
    first = hand[0]
    for card in hand:
        if first.suit != card.suit:
            return False
    return True


def change(stock):
    cards = []
    n = int(input("何枚変えますか？>>>"))
    for i in range(n):
        card = stock.pop()
        cards.append(card)
    return cards


stock = new_stock()

cards = take_cards(stock, 5)
print(f"手札: {cards}")

cards = change(stock)

print(f"手札: {cards}")
