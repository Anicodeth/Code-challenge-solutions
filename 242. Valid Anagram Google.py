class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = Counter(s)
        tCount = Counter(t)

        for key in sCount:
            if sCount[key] != tCount[key]:
                return False

        for key in tCount:
            if sCount[key] != tCount[key]:
                return False

        return True 
        
