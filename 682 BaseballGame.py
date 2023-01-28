class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for i in operations:
            print(i, i[0])
            if i=="C":
                stack.pop(-1)
            elif i=="D":
                stack.append(stack[-1]*2)
            elif i=="+":
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(i))
        return sum(stack)
