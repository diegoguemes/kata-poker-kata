from poker_hands import *

class PokerHandTranslator:

    def translate(self, hand):
        if self.__is_pair(hand):
            return PAIR
        return HIGH_CARD

    def __is_pair(self, hand):
        values = [card[:-1] for card in hand]
        return len(set(values)) == len(hand) - 1