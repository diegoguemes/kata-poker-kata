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
        return self.__distinct_values_count(hand) == len(hand) - 1

    def __is_two_pair(self, hand):
        return self.__distinct_values_count(hand) == len(hand) - 2

    def __is_three_of_a_kind(self, hand):
        return self.__max_repeated_value_count(hand) == 3

    def __is_straight(self, hand):
        values = self.__values_of(hand)
        return sorted(values) == list(range(min(values), max(values) + 1))

    def __distinct_values_count(self, hand):
        return len(set(self.__values_of(hand)))

    def __max_repeated_value_count(self, hand):
        max_count = 0
        values = self.__values_of(hand)
        for value in set(values):
            count = values.count(value)
            if count > max_count:
                max_count = count
        return max_count

    def __values_of(self, hand):
        return [self.__value_of(card) for card in hand]

    def __value_of(self, card):
        value = card[:-1]
        court_carts = {'J': 11, 'Q': 12, 'K': 13, 'A':14}
        if value.isdigit():
            return int(value)
        return court_carts[value]