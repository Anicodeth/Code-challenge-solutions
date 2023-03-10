class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for pos, v in sorted(zip(position, speed),reverse = True):

            dist = target - pos
            time = dist / v 
            
            if not stack:
                stack.append(time)
            elif time > stack[-1]:
                stack.append(time)

        return len(stack)
