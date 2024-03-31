class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isPalindrome(segment):
            l, r = 0, len(segment) - 1
            while l <= r:
                if segment[l] != segment[r]:
                    return False
                
                l += 1
                r -= 1

            return True


        def backtrack(s, curr):
            
            if not s:
                res.append(curr[:])
                return

            for i in range(len(s)):
                segment = s[:i + 1]
                if isPalindrome(segment):
                    curr.append(segment)
                    backtrack(s[i + 1:], curr)
                    curr.pop()

        res = []

        backtrack(s, [])

        return res
        
