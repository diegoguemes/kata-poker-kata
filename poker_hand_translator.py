from poker_hands import *

class PokerHandTranslator:

    def translate(self, hand):
        values = set([card[:-1] for card in hand])
        if len(values) == len(hand) - 1:
            return PAIR
        return HIGH_CARD