class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        return len(count.keys()) == len(set(count.values()))
        
