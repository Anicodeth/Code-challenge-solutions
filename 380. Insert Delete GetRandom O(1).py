class RandomizedSet:

    def __init__(self):
        self.randomSet = set()
        

    def insert(self, val: int) -> bool:
        if val in self.randomSet:
            return False
        else:
            self.randomSet.add(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.randomSet:
            self.randomSet.remove(val)
            return True
        else:
            return False       

    def getRandom(self) -> int:
        return random.choice(list(self.randomSet))
        
