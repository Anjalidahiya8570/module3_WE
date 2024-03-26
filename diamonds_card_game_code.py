# -*- coding: utf-8 -*-
"""Diamonds_card_game.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NlWTlzWV5T1ParN8sEhxpPUDswAQXOhB
"""

import random

suits = ("Clubs", "Diamonds", "Hearts", "Spades")
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")
deck = []

# Create the deck
for suit in suits:
    for rank in ranks:
        deck.append(rank + " of " + suit)

def deal_cards(players):
  """Deals cards to players"""
  hands = []
  for _ in range(players):
    hand = random.sample(deck, len(deck) // players)
    hands.append(hand)
  return hands

def display_hand(hand):
  """Shows player's hand"""
  print("Your hand:")
  for card in hand:
    print("-", card)

def get_bid(player_hand):
  """Gets player's bid"""
  while True:
    try:
      bid = int(input("Enter your bid (number of tricks): "))
      if 0 <= bid <= len(player_hand):
        return bid
      else:
        print("Invalid bid. Please enter a number between 0 and", len(player_hand))
    except ValueError:
      print("Invalid input. Please enter a number.")

def get_ai_bid(ai_hand):
  """Simulates AI's bid based on hand strength"""
  diamonds = sum(1 for card in ai_hand if "Diamonds" in card)
  high_cards = sum(1 for card in ai_hand if card.split()[0] in ["Queen", "King", "Ace"])
  return min(len(ai_hand), diamonds + high_cards // 2)

def play_trick(player_hand, ai_hand, led_suit):
  """Plays a single trick"""
  player_card = input("Play a card (e.g., 7 of Spades): ")
  while player_card not in player_hand:
    print("Invalid card. Please play a card from your hand.")
    player_card = input("Play a card: ")
  player_hand.remove(player_card)

  ai_card = random.choice([card for card in ai_hand if (suits[ranks.index(player_card.split()[0])] == led_suit) or ("Diamonds" in card)])
  ai_hand.remove(ai_card)

  if suits[ranks.index(player_card.split()[0])] == led_suit:
    if suits[ranks.index(ai_card.split()[0])] == led_suit and ranks.index(player_card.split()[0]) > ranks.index(ai_card.split()[0]):
      print("You win the trick!")
      return player_hand, ai_hand, player_card
    else:
      print("You win the trick!")
      return player_hand, ai_hand, player_card
  else:
    if "Diamonds" in ai_card:
      print("AI wins the trick with", ai_card)
      return player_hand, ai_hand, ai_card
    else:
      print("You win the trick!")
      return player_hand, ai_hand, player_card

def play_game():
  """Main game loop"""
  random.shuffle(deck)
  player_hand, ai_hand = deal_cards(2)

  display_hand(player_hand)
  player_bid = get_bid(player_hand)
  ai_bid = get_ai_bid(ai_hand)

  print("Your bid:", player_bid)
  print("AI's bid:", ai_bid)

  # Trick loop
  for _ in range(len(player_hand)):
    led_suit = None
    if _ == 0:
      print("You lead the first trick.")
    else:
      winning_card = tricks[-1][-1]
      led_suit = winning_card.split()[1]
      print("The leading suit is", led_suit)

    player_hand, ai_hand, trick_winner = play_trick(player_hand.copy(), ai_hand.copy(), led_suit)
    tricks.append([player_card, ai_card, trick_winner])

deal_cards(2)

my_hand = deal_cards(2)[0]
display_hand(my_hand)