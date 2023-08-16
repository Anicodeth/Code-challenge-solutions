class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
      if not nums:
        return []
      window = [ (-nums[i], i) for i in range(k)]
      heapq.heapify(window)
      res = [-window[0][0]]

      for i in range(k, len(nums)):
        while window and window[0][1] <= i-k:
          heapq.heappop(window)

        heapq.heappush(window, (-nums[i],i))
        res.append(-window[0][0])
      return res
