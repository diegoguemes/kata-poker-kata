from poker_hands import *

class PokerHandTranslator:
    def __init__(self):
        self.hand_rules = sorted({
            STRAIGHT: self.__is_straight,
            THREE_OF_A_KIND: self.__is_three_of_a_kind,
            TWO_PAIR: self.__is_two_pair,
            PAIR: self.__is_pair
        }.items(), reverse=True)

    def translate(self, hand):
        for hand_type, hand_rule in self.hand_rules:
            if hand_rule(hand):
                return hand_type
        return HIGH_CARD

    def __is_pair(self, hand):
        return hand.distinct_values_count() == 4

    def __is_two_pair(self, hand):
        return hand.distinct_values_count() == 3

    def __is_three_of_a_kind(self, hand):
        return hand.max_repeated_value_count() == 3

    def __is_straight(self, hand):
        values = hand.values()
        return sorted(values) == list(range(min(values), max(values) + 1))