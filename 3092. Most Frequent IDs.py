class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        heap = []
        dic = defaultdict(int)
        ans = []

        for num, freq in zip(nums, freq):
            dic[num] += freq
            heapq.heappush(heap, (-dic[num], num))
            while -heap[0][0] != dic[heap[0][1]]:
                heapq.heappop(heap) 

            if not heap:
                ans.append(0)
            else:
                ans.append(-heap[0][0])

        return ans


        
