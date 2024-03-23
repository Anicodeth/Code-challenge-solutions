class Logger:

    def __init__(self):
        self.stamps = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:

        if message not in self.stamps:
            self.stamps[message] = timestamp + 10
            return True

        last = self.stamps[message]
        if last <= timestamp:
            self.stamps[message] = timestamp + 10
            return True
        
        return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
