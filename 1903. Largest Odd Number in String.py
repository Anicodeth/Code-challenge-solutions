class Solution:
    def largestOddNumber(self, num: str) -> str:

        largest = ""
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                largest = num[:i + 1]
                break

        return largest
