import unittest
from poker_hands import *
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

    def translate(self, hand):
        return self.poker_hand_translator.translate(hand)


if __name__ == '__main__':
    unittest.main()
