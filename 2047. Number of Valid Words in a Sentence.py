class Solution:
    def countValidWords(self, sentence: str) -> int:
        def is_valid(word):
            if not word:
                return True
            if word[0] == '-' or word[-1] == '-' or word.count('-') > 1:
                return False
            for c in word:
                if (ord(c) < ord('a') or ord(c) > ord('z')) and ord(c) != ord('-'):
                    return False
            return True

        words = sentence.split(' ')
        count = 0

        for word in words:
            
            if not word:
                continue
            if word[-1] == '.' or word[-1] == ',' or word[-1] == '!':
                word = word[:-1]
            if is_valid(word):
                count += 1

        return count


        
