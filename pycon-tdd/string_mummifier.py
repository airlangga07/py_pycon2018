class StringMummifier:
    def mummify(self, word):
        vowels = [ x for x in word if x in 'aiueo' ]

        if len(word) == 0:
            return ''

        if len(vowels) / len(word) < 0.3:
            return word
        
        result = []

        for x in range(len(word)):
            if (char not in 'aiueo'):
                result.append(char)
            else:
        
        return ''.join(result)