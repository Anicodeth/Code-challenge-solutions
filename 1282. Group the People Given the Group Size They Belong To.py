class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        divisions = defaultdict(list)

        for i, group in enumerate(groupSizes):
            divisions[group].append(i)

        res = []
        for size in divisions:
            n = len(divisions[size])
            if size == n:
                res.append(divisions[size])
            else:
                for i in range(0, n - size + 1,size):
                    res.append(divisions[size][i:i + size])
        return res

        
