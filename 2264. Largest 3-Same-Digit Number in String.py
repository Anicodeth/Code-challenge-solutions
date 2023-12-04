class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        curr = deque(num[:3])
        largest = curr[0] if len(set(curr)) == 1 else ""
        for i in range(1, len(num) - 2):
            curr.append(num[i + 2])
            curr.popleft()
            if len(set(curr)) == 1 and not largest:
                largest = curr[0]
            elif len(set(curr)) == 1 and int(curr[0]) > int(largest):
                largest = curr[0]

        return largest * 3
