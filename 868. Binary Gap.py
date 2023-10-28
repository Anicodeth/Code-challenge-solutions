class Solution:
    def binaryGap(self, n: int) -> int:
        binary_str = bin(n)[2:]  
        found_first_one = False
        max_distance = 0

        for i in range(len(binary_str)):
            if binary_str[i] == '1':
                if found_first_one:
                    distance = i - start
                    start = i
                    max_distance = max(max_distance, distance)
                else:
                    start = i
                    found_first_one = True

        return max_distance
