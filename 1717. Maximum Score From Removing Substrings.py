class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        
        def removeSeq(word, first, second, value):
            stack = []
            countPairs = 0

            for c in word:
                if not stack or stack[-1] != first or c != second:
                    stack.append(c)
                elif stack and stack[-1] == first and c == second:
                    stack.pop()
                    countPairs += 1

            return "".join(stack), countPairs * value

        res = 0

        if x > y:
            newString, value = removeSeq(s, 'a', 'b', x)
            res += value
            _ , value = removeSeq(newString, 'b', 'a', y)
            res += value    
        else:
            newString, value = removeSeq(s, 'b', 'a', y)
            res += value
            _ , value = removeSeq(newString, 'a', 'b', x)
            res += value 

        return res


        
                




            

