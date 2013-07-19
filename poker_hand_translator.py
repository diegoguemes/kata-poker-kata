from poker_hands import *
from poker_hand_rules import *

class HandTranslator:
    def __init__(self, hand_rules):
        self.hand_rules = hand_rules

    def translate(self, hand):
        for hand_type, hand_rule in self.hand_rules:
            if hand_rule(hand):
                return hand_type
        return None

def create_poker_hand_translator():
    poker_hand_rules = sorted({
        HIGH_CARD: HighCardRule().is_satisfied_by,
        PAIR: PairRule().is_satisfied_by,
        TWO_PAIR: TwoPairRule().is_satisfied_by,
        THREE_OF_A_KIND: ThreeOfAKindRule().is_satisfied_by,
        STRAIGHT: StraightRule().is_satisfied_by,
        FLUSH: FlushRule().is_satisfied_by,
        FULL_HOUSE: FullHouseRule().is_satisfied_by,
        FOUR_OF_A_KIND: FourOfAKindRule().is_satisfied_by,
        STRAIGHT_FLUSH: StraightFlushRule().is_satisfied_by,
        ROYAL_FLUSH: RoyalFlushRule().is_satisfied_by
    }.items(), reverse=True)
    return HandTranslator(poker_hand_rules)