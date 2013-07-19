class PokerHand:
    def __init__(self, cards):
        self.__cards = cards

    def distinct_values_count(self):
        return len(set(self.values()))

    def distinct_suits_count(self):
        return len(set(self.suits()))

    def max_repeated_value_count(self):
        max_count = 0
        values = self.values()
        for value in set(values):
            count = values.count(value)
            if count > max_count:
                max_count = count
        return max_count

    def values(self):
        return [self.__value_of(card) for card in self.__cards]

    def suits(self):
        return [card[-1:] for card in self.__cards]

    def __value_of(self, card):
        value = card[:-1]
        court_carts = {'J': 11, 'Q': 12, 'K': 13, 'A':14}
        if value.isdigit():
            return int(value)
        return court_carts[value]