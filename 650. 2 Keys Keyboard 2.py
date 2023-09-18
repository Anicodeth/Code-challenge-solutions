class Solution:
    def minSteps(self, n: int) -> int:
        @cache
        def dp(curr, clip, op, steps):
            if curr == n:
                return steps
            elif curr > n:
                return inf

            steps += 1

            if op == 'C':
                mini = dp(curr, clip, 'P', steps )
            elif op == 'P':
                copied = dp(curr + clip, curr + clip, 'C', steps  )
                pasted = dp(curr + clip, clip, 'P', steps  )
                mini = min(copied, pasted)

            return mini


        return dp(1,1,'C',0)
        
