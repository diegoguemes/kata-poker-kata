import unittest
from poker_hands import *
from poker_hand import PokerHand
from poker_hand_translator import PokerHandTranslator


class PokerHandTranslatorTest(unittest.TestCase):

    def setUp(self):
        self.poker_hand_translator = PokerHandTranslator()

    def test_translates_high_card_hand(self):
        self.assertEqual(HIGH_CARD, self.translate(['A♥', 'K♥', 'Q♣', '10♥', '2♠']))

    def test_translates_pair_hand(self):
        self.assertEqual(PAIR, self.translate(['2♦', '2♥', 'Q♥', '7♥', '6♣']))

    def test_translates_two_pair_hand(self):
        self.assertEqual(TWO_PAIR, self.translate(['K♣', 'K♠', '9♥', '9♦', 'J♥']))

    def test_translates_three_of_a_kind_hand(self):
        self.assertEqual(THREE_OF_A_KIND, self.translate(['3♣', '3♠', '3♥', 'Q♦', '2♥']))

    def test_translates_straight_hand(self):
        self.assertEqual(STRAIGHT, self.translate(['9♣', '8♦', '7♠', '6♥', '5♣']))

    def test_translates_flush_hand(self):
        self.assertEqual(FLUSH, self.translate(['A♠', 'J♠', '10♠', '6♠', '3♠']))

    def test_translates_full_house_hand(self):
        self.assertEqual(FULL_HOUSE, self.translate(['5♠', '5♥', '5♦', '8♠', '8♥']))

    def test_translates_four_of_a_kind_hand(self):
        self.assertEqual(FOUR_OF_A_KIND, self.translate(['5♠', '5♥', '5♦', '5♣', '8♥']))

    def test_translates_straight_flush_hand(self):
        self.assertEqual(STRAIGHT_FLUSH, self.translate(['J♣', '10♣', '9♣', '8♣', '7♣']))

    def test_translates_royal_flush_hand(self):
        self.assertEqual(ROYAL_FLUSH, self.translate(['A♣', 'K♣', 'Q♣', 'J♣', '10♣']))

    def translate(self, hand):
        return self.poker_hand_translator.translate(PokerHand(hand))


if __name__ == '__main__':
    unittest.main()
