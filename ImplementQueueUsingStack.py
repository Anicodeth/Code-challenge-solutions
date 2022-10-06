class MyQueue:

    def __init__(self):
        self.que=[]

    def push(self, x: int) -> None:
        self.que.append(x)
       
    def pop(self) -> int:
        return self.que.pop(0) 
        
    def peek(self) -> int:
        return self.que[0]

    def empty(self) -> bool:
        return (True if not self.que else False)
