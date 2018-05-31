from unittest import TestCase

from string_mummifier import StringMummifier


class TestStringMummifier(TestCase):
    def test_should_not_mummify_empty_string(self):
        word = ""

        mummifier = StringMummifier()
        mummified_word = mummifier.mummify(word)

        self.assertEqual(word, mummified_word)
    

    def test_should_not_mummify_string_less_than_thirty(self):
        input_word = 'abcdd'

        mummifier = StringMummifier()
        mummified_word = mummifier.mummify(input_word)

        self.assertEqual(input_word, mummified_word)


    def test_should_mummify_string_more_than_thirty(self):
        input_word = 'his'
        result_word = 'hmummys'

        mummifier = StringMummifier()
        mummified_word = mummifier.mummify(input_word)

        self.assertEqual(result_word, mummified_word)