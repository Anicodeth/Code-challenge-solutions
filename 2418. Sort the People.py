class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pairs = list(zip(names, heights))
        pairs.sort(key = lambda x: -x[1])
        res = [ pair[0] for pair in pairs]

        return res
        
        
