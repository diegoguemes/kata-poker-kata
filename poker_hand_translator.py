from poker_hands import *
from poker_hand_rules import *

class HandTranslator:
    def __init__(self, hand_rules):
        self.hand_rules = hand_rules

    def translate(self, hand):
        for hand_type, hand_rule in self.hand_rules:
            if hand_rule.is_satisfied_by(hand):
                return hand_type
        return None

def create_poker_hand_translator():
    poker_hand_rules = sorted({
        HIGH_CARD: HighCardRule(),
        PAIR: PairRule(),
        TWO_PAIR: TwoPairRule(),
        THREE_OF_A_KIND: ThreeOfAKindRule(),
        STRAIGHT: StraightRule(),
        FLUSH: FlushRule(),
        FULL_HOUSE: FullHouseRule(),
        FOUR_OF_A_KIND: FourOfAKindRule(),
        STRAIGHT_FLUSH: StraightFlushRule(),
        ROYAL_FLUSH: RoyalFlushRule()
    }.items(), reverse=True)
    return HandTranslator(poker_hand_rules)