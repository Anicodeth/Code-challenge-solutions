class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        binary_str = bin(n)[2:][::-1]  
        even_count = 0
        odd_count = 0

        for i in range(len(binary_str)):
            if i % 2 == 0:
                if binary_str[i] == "1":
                    even_count += 1
            else:
                if binary_str[i] == "1":
                    odd_count += 1

        return [even_count, odd_count]
        
