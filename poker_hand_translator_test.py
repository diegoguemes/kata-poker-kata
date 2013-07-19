import unittest

class PokerHandTranslatorTest(unittest.TestCase):
    def test_translates_high_card_hand(self):
        self.assertEqual(HIGH_CARD, self.translate(['A♥', 'K♥', 'Q♣', '10♥', '2♠']))

if __name__ == '__main__':
    unittest.main()
