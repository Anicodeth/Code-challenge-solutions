class Solution:
    def minDeletions(self, s: str) -> int:
        dic = {}
        for c in s:
            dic[c] = dic.get(c, 0) + 1

        held = set()
        operations = 0
        for c in dic:
            if dic[c] in held:
                while dic[c] in held and dic[c] != 0:
                  dic[c] = dic.get(c, 0) - 1  
                  operations += 1

            held.add(dic[c])
        return operations

        
