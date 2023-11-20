class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
            char_count = {}

            for char in chars:
                char_count[char] = char_count.get(char, 0) + 1

            def can_form(word):
                word_count = {}
                for char in word:
                    word_count[char] = word_count.get(char, 0) + 1
                    if char_count.get(char, 0) < word_count[char]:
                        return False
                return True

            sum_lengths = 0
            for word in words:
                if can_form(word):
                    sum_lengths += len(word)

            return sum_lengths
