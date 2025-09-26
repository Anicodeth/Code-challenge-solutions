class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefix = [0] * n

        for op in shifts:
            prefix[op[0]] += 1 if op[2] else -1
            if op[1] + 1 < n:
                prefix[op[1] + 1] -= 1 if op[2] else -1

        for i in range(1, n):
            prefix[i] += prefix[i - 1]

        new = []

        for i, c in enumerate(s):
            augmentedS = chr(((ord(c) - 97 + prefix[i]) % 26) + 97)
            new.append(augmentedS)

        return "".join(new)        
        
