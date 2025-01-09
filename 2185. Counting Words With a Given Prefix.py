class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        def is_pref(pref, word):
            n, m = len(pref), len(word)
            p1, p2 = 0, 0

            while p1 < n and p2 < m:
                if pref[p1] != word[p2]:
                    return False

                p1 += 1
                p2 += 1

            if p1 < n: return False

            return True

        count = 0 
        for word in words:
            if is_pref(pref, word):
                count += 1

        return count 
