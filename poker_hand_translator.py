from poker_hands import *

class PokerHandTranslator:
    def __init__(self):
        self.hand_rules = sorted({
            ROYAL_FLUSH: self.__is_royal_flush,
            STRAIGHT_FLUSH: self.__is_straight_flush,
            FOUR_OF_A_KIND: self.__is_four_of_a_kind,
            FULL_HOUSE: self.__is_full_house,
            FLUSH: self.__is_flush,
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

    def __is_flush(self, hand):
        return hand.distinct_suits_count() == 1

    def __is_full_house(self, hand):
        return hand.max_repeated_value_count() == 3 and hand.distinct_values_count() == 2

    def __is_four_of_a_kind(self, hand):
        return hand.max_repeated_value_count() == 4

    def __is_straight_flush(self, hand):
        return self.__is_straight(hand) and self.__is_flush(hand)

    def __is_royal_flush(self, hand):
        return self.__is_straight_flush(hand) and hand.contains_value('A')