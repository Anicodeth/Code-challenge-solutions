class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        even = odd = count = running = 0

        for num in arr:
            running += num
            oddCheck = (running % 2 == 1)

            if oddCheck:
                count += (1 + even)
                odd += 1
            else:
                count += odd
                even += 1
            
        return count % (10**9 + 7)
