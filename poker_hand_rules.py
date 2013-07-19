class HighCardRule:
    def is_satisfied_by(self, hand):
        return True

class PairRule:
    def is_satisfied_by(self, hand):
        return hand.distinct_values_count() == 4

class TwoPairRule:
    def is_satisfied_by(self, hand):
        return hand.distinct_values_count() == 3

class ThreeOfAKindRule:
    def is_satisfied_by(self, hand):
        return hand.max_repeated_value_count() == 3

class StraightRule:
    def is_satisfied_by(self, hand):
        values = hand.values()
        return sorted(values) == list(range(min(values), max(values) + 1))

class FlushRule:
    def is_satisfied_by(self, hand):
        return hand.distinct_suits_count() == 1

class FullHouseRule:
    def is_satisfied_by(self, hand):
        return hand.max_repeated_value_count() == 3 and hand.distinct_values_count() == 2

class FourOfAKindRule:
    def is_satisfied_by(self, hand):
        return hand.max_repeated_value_count() == 4

class StraightFlushRule:
    def is_satisfied_by(self, hand):
        return StraightRule().is_satisfied_by(hand) and FlushRule.is_satisfied_by(hand)

class RoyalFlushRule:
    def is_satisfied_by(self, hand):
        return StraightFlushRule().is_satisfied_by(hand) and hand.contains_value('A')
