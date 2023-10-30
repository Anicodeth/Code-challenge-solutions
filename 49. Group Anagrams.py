class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        table = defaultdict(list)

        for word in strs:
            pruned = "".join(sorted(word))
            table[pruned].append(word)

        return table.values()

            
        
