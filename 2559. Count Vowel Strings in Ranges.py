class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix = [0]
        v = set(['a', 'e', 'i', 'o', 'u'])

        for word in words:
            if word[-1] in v and word[0] in v:
                prefix.append(prefix[-1] + 1)
            else:
                prefix.append(prefix[-1])   

        ans = []
        for query in queries:
            ans.append(prefix[query[1] + 1] - prefix[query[0]])

        return ans
