class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s=sum(nums[:k])
        maxavg=s/k
        for i in range(1,len(nums)-k+1):
          news=((s+nums[i+k-1])-nums[i-1])
          locavg = news/k
          s=news
          
          if locavg > maxavg:
            maxavg = locavg
        return maxavg
