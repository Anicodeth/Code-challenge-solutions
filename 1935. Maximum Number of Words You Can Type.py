class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        notWorking = set([ c for c in brokenLetters ])
        words = text.split(" ")
        count = 0 

        for word in words:
            valid = True
            for c in word:
                if c in notWorking:
                    valid = False
                    break

            if valid: count += 1

        return count

        
