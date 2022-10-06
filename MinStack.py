class MinStack:

    def __init__(self):
        self.stalk=[]
        self.minstalk=[]

    def push(self, val: int) -> None:
        self.stalk.append(val)
        val=min(val,self.minstalk[-1] if self.minstalk else val)
        self.minstalk.append(val)

    def pop(self) -> None:
        self.stalk.pop()
        self.minstalk.pop()
        

    def top(self) -> int:
        return self.stalk[-1]

    def getMin(self) -> int:
        return self.minstalk[-1]
