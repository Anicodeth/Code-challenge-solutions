
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        possible = []
        total_speed, max_performance = 0, 0

        ordered = list(zip(efficiency, speed))
        ordered.sort(reverse = True)
        
        for eff, spd in ordered:
            heapq.heappush(possible, spd)
            total_speed += spd
            
            if len(possible) > k:
                total_speed -= heapq.heappop(possible)
                
            max_performance = max(max_performance, total_speed * eff)
        
        return max_performance % (10**9 + 7)
