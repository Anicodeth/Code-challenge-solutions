class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        flag = groups[0]
        res = [words[0]]
        for i in range(1, n):
            if groups[i] != flag:
                res.append(words[i])
                flag = not flag

        return res

        
