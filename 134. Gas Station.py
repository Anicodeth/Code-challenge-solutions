class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
            totalGas = 0
            currentGas = 0
            start = 0
            totalCost = 0

            for i in range(len(gas)):
                currentGas += gas[i] - cost[i]
                totalCost += cost[i]
                totalGas += gas[i]

                if currentGas < 0:
                    start = i + 1
                    currentGas = 0

            if totalGas >= totalCost:
                return start
            else:
                return -1
