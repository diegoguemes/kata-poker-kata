import unittest
from poker_hands import *
from poker_hand_translator import PokerHandTranslator

class PokerHandTranslatorTest(unittest.TestCase):

    def setUp(self):
        self.poker_hand_translator = PokerHandTranslator()

    def test_translates_high_card_hand(self):
        self.assertEqual(HIGH_CARD, self.translate(['A♥', 'K♥', 'Q♣', '10♥', '2♠']))

    def translate(self, hand):
        return self.poker_hand_translator.translate(hand)


if __name__ == '__main__':
    unittest.main()
