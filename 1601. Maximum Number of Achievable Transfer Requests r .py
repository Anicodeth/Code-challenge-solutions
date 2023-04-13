class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
      def backtrack(request_idx, counts):
            if request_idx == len(requests):
                if all(c == 0 for c in counts):
                    return 0
                return float('-inf')
            
            from_building, to_building = requests[request_idx]
            ans = backtrack(request_idx + 1, counts)
            counts[from_building] -= 1
            counts[to_building] += 1
            ans = max(ans, backtrack(request_idx + 1, counts) + 1)
            counts[from_building] += 1
            counts[to_building] -= 1
            return ans
        
      return max(backtrack(0, [0] * n), 0)
