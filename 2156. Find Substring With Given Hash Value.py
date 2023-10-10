class Solution:
    def subStrHash(self, s: str, base: int, mod: int, length: int, target_hash: int) -> str:
        current_hash = 0
        multiplier = 1

        for i in range(length):
            current_hash = current_hash + (ord(s[i]) - ord('a') + 1) * multiplier
            multiplier = multiplier * base
        
        multiplier = multiplier // base
        
        for j in range(len(s) - length + 1):
            if current_hash % mod == target_hash:
                return s[j:j+length]
            
            if j < len(s) - length:
                current_hash = (current_hash - (ord(s[j]) - ord('a') + 1)) // base + (ord(s[j+length]) - ord('a') + 1) * multiplier
        
        return ""
