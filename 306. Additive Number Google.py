class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def is_valid(num):
            return len(num) == 1 or (num[0] != '0' and int(num) != 0)

        def backtrack(num, curr):
            if not num and len(curr) >= 3:
                return True
            for i in range(1, len(num) + 1):
                if (len(curr) < 2 or int(num[:i]) == curr[-1] + curr[-2]) and is_valid(num[:i]):
                    curr.append(int(num[:i]))
                    if backtrack(num[i:], curr):
                        return True
                    curr.pop()
            return False

        return backtrack(num, [])
