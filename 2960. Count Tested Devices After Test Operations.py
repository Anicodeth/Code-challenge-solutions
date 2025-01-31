class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        count = 0
        n = len(batteryPercentages)

        for i in range(n):
            if batteryPercentages[i] > 0:
                count += 1
                for j in range(i + 1, n):
                    batteryPercentages[j] -= 1
                    
        return count
        
