class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        dic = {}
        n = len(pattern)
        words = s.split(" ")
        visit = set()
        if len(words) != n: return False
        for p in range(n):
            if pattern[p] in dic:
                if dic[pattern[p]] != words[p]:
                    return False
            else:
                if words[p] in visit:
                    return False
                dic[pattern[p]] = words[p]
                visit.add(words[p])

        return True
