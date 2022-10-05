class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        notes={
            "+":operator.add,
            "-":operator.sub,
            "/":operator.truediv,
            "*":operator.mul
        }
        stalk=[]

        for i in tokens:
            if i not in notes:
                stalk.append(int(i))
            else:
                right=stalk.pop()
                left=stalk.pop()
                stalk.append(int(notes[i](left,right)))

        return stalk.pop()
