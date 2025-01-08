class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        def is_valid(str1, str2):

            p1, p2 = 0, 0
            n, m = len(str1), len(str2)

            while p1 < n and p2 < m:
                if str1[p1] != str2[p2]:
                    return False

                p1 += 1
                p2 += 1

            if p1 < n: return False

            p1, p2 = n - 1, m - 1

            while p1 >= 0 and p2 >= 0:
                if str1[p1] != str2[p2]:
                    return False

                p1 -= 1
                p2 -= 1
                
            if p1 >= 0: return False

            return True


        size = len(words)
        count = 0

        for i in range(size):
            for j in range(i + 1, size):
                if is_valid(words[i], words[j]):
                    count += 1

        return count
        
