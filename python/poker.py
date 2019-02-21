

# PRACTICE

# poker game

import random
from enum import Enum
from functools import total_ordering
from collections import defaultdict

@total_ordering
class Suit(Enum):
  spade = 0
  club = 1
  heart = 2
  diamond = 3

  def __repr__(self):
    return self.name

  def __lt__(self, other):
    if self.__class__ is other.__class__:
      return self.value < other.value
    return NotImplemented

@total_ordering
class Face(Enum):
  ace = 1
  two = 2
  three = 3
  four = 4
  five = 5
  six = 6
  seven = 7
  eight = 8
  nine = 9
  ten = 10
  jack = 11
  queen = 12
  king = 13

  def __repr__(self):
    return self.name

  def __lt__(self, other):
    if self.__class__ is other.__class__:
      return self.value < other.value
    return NotImplemented


@total_ordering
class Card(object):
  def __init__(self, suit, face):
    self.suit = suit
    self.face = face

  def __repr__(self):
    return str((self.suit, self.face))

  def __eq__(self, other):
    if self.__class__ is other.__class__:
      return self.value() == other.value()
    return NotImplemented

  def __lt__(self, other):
    if self.__class__ is other.__class__:
      return self.value() < other.value()
    return NotImplemented

  def value(self):
    return self.face.value + self.suit.value * 0.25

class Deck(object):
  def __init__(self):
    self.new_pack()
    self.shuffle()

  # open a new pack of cards, resetting library and discard piles
  def new_pack(self):
    self.discard = []
    self.library = self.n_decks(1)

  # generate n new decks of cards
  def n_decks(self, n=1):
    cards = []
    for suit in Suit:
      for face in Face:
        cards.append(Card(suit.value, face.value))
    return cards

  def shuffle(self, include_discard=True):
    self.library += self.discard
    self.discard = []
    for i in range(len(self.library) - 1):
      j = random.randint(i, len(self.library))
      tmp_card = self.library[i]
      self.library[i] = self.library[j]
      self.library[j] = tmp_card

  def draw(self, n=1):
    cards = []
    for i in range(n):
      # could slice to speed up, this seems more readable
      cards.append(self.libary.pop())
    return cards

  def discard(self, cards):
    self.discard += cards


@total_ordering
class Hand(object):
  def __init__(self, starting_cards):
    self.hand_size = 5
    self.cards = []
    self.add_cards(starting_cards)

  def add_cards(self, cards):
    self.cards += cards
    self.update_cards()

  # run whenever we add or remove cards
  def update_cards(self):
    self.suits = defaultdict(int)
    self.faces = defaultdict(int)
    for card in self.cards:
      self.suits[card.suit] += 1
      self.faces[card.face] += 1

    # e.g. self.groups[2] = ['5', 'queen'] (list of pairs by 'face')
    self.groups = defaultdict(list)
    for face, num in self.faces.items():
      self.groups[num] += [face]

    self.hi_card = max(self.cards, key=lambda c: c.value())

    self.is_flush = self.is_flush()
    self.is_straight = self.is_straight()

  def is_flush(self):
    return max(self.suits.values()) == self.hand_size

  def is_straight(self):
    i = 1
    while i < len(self.cards):
      if self.cards[i].face.value != self.cards[i-1].face.value + 1:
        return False
      return True

  def score(self):
    # royal flush # 8000 + hi_card
    # straight flush
    if self.is_flush:
      if self.is_straight:
        return 8000 + self.hi_card.value()

    # four of a kind # 7000 + four_card
    if self.groups[4]:
      return 7000 + self.groups[4][0].value

    # full house # 6000 + 15 * trip_card + pair_card
    if self.groups[3] and self.groups[2]:
      return 6000 + self.groups[3][0].value * 15 + self.groups[2][0].value

    # flush # 5000 + hi_card
    if self.is_flush:
      return 5000 + self.hi_card.value()

    # straight # 4000 + hi_card
    if self.is_straight:
      return 4000 + self.hi_card.value()

    # three of a kind # 3000 + trip_card
    if self.groups[3]:
      return 3000 + self.groups[3][0].value

    # two pair # 2000 + hi_pair_card
    if self.groups[2] and len(self.groups[2] > 1):
      return 2000 + max(self.groups[2], key=lambda g: g.value).value

    # pair # 1000 + pair_card
    if self.groups[2]:
      return 1000 + self.groups[2][0].value

    # high card # hi_card
    return self.hi_card.value()

  def __eq__(self, other):
    if self.__class__ is other.__class__:
      return self.score() == other.score()
    return NotImplemented

  def __lt__(self, other):
    if self.__class__ is other.__class__:
      return self.score() < other.score()
    return NotImplemented

  def __repr__(self):
    return str([self.cards, self.score()])


