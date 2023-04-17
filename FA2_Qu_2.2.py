import unittest

class TestPangram (unittest.TestCase):

    #This is going to test if a sentance is a valid pangram
    def test_pangram_true(self):
        input1 = "The quick brown fox jumps over the lazy dog"
        self.assertTrue(pangram(input1))

    # This is going to test if a sentance is a non-pangram
    def test_pangram_false(selfself):
        input2 = "The quick brown fox jumps over the lazy duck"
        self.assertTrue(pangram(input2))

    # This will test a sentance with numbers and symbols
    def test_pangram_numbersymbol(self):
        input3 = "The @!ick b$%^&n F04 jump5 ove4 t@e lazy DOG"
        self.assertFalse(pangram(input3))

    if __name__ == '__ main__':
        unittest.main()




