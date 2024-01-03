class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        stack = []
        count = 0

        for row in bank:
            if not stack:
                stack.append(row.count('1'))
            else:
                curr = row.count('1')
                if curr == 0:
                    continue
                count += stack[-1] * curr
                stack.append(curr)

        return count

            
            
        
