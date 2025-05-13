class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        dic = defaultdict(list)
        arr.sort()

        for i in range(len(arr) - 1):
            dif = abs(arr[i] - arr[i + 1])
            dic[dif].append([arr[i], arr[i + 1]])

        mapping = list(dic.items())
        mapping.sort(key = lambda x: x[0])

        return mapping[0][1]
        
