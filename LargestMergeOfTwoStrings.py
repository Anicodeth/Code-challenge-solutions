class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        if word1 >= word2 > '':
            return word1[0] + self.largestMerge(word1[1:], word2)
        if word2 >= word1 > '':
            return word2[0] + self.largestMerge(word1, word2[1:])
        return word1 + word2
