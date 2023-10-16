class Solution:
    def countVowels(self, word: str) -> int:
        total_count = 0
        word_length = len(word)
        
        for start_pos in range(word_length):
            if word[start_pos] in 'aeiou':
                total_count += (word_length - start_pos) * (start_pos + 1)
        
        return total_count
