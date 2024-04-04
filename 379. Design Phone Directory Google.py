class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.slots = [i for i in range(maxNumbers)]
        self.open  = set(self.slots)

        
    def get(self) -> int:
        if not self.slots:
            return -1
        slot =  self.slots.pop()
        self.open.remove(slot)
        return slot

    def check(self, number: int) -> bool:
        if number in self.open:
            return True
        else: 
            return False


    def release(self, number: int) -> None:
        if number in self.open:
            return 
        self.slots.append(number)
        self.open.add(number)

        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
