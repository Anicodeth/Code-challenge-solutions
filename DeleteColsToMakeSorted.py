from collections import defaultdict
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        col=defaultdict(list)
        for string in strs:
            for i,c in enumerate(string):
                col[i].append(c)

        count=0

        for co in col:
            print(sorted(col[co]),col[co])
            if col[co]==sorted(col[co]):
                count+=1

        return len(strs[0])-count
