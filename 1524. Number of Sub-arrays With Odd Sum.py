class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        answer = 0
        running_sum, oddcount, evencount = 0, 0, 0
        
        for num in arr:
            running_sum += num
            if running_sum % 2:
                oddcount += 1
                answer += evencount + 1
            else:
                evencount += 1
                answer += oddcount

        return answer % (10 ** 9 + 7)
