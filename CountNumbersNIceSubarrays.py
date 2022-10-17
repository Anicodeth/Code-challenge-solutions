class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
            dic = { 0: 1 }
            cnt = res = 0
            for idx, num in enumerate(nums):
                if num % 2 == 1:
                    cnt += 1

                if cnt - k in dic:
                    res += dic[cnt-k]

                dic[cnt] = dic.get(cnt, 0) + 1

