from poker_hands import *

class PokerHandTranslator:

    def translate(self, hand):
        if self.__is_three_of_a_kind(hand):
            return THREE_OF_A_KIND
        if self.__is_two_pair(hand):
            return TWO_PAIR
        if self.__is_pair(hand):
            return PAIR
        return HIGH_CARD

    def __is_pair(self, hand):
        return self.__distinct_values_count(hand) == len(hand) - 1

    def __is_two_pair(self, hand):
        return self.__distinct_values_count(hand) == len(hand) - 2

    def __is_three_of_a_kind(self, hand):
        max = 0
        values = [card[:-1] for card in hand]
        for value in set(values):
            count = values.count(value)
            if count > max:
                max = count
        return max == 3

    def __distinct_values_count(self, hand):
        values = [card[:-1] for card in hand]
        return len(set(values))