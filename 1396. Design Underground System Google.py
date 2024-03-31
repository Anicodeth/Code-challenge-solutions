class UndergroundSystem:

    def __init__(self):
        self.customerHistory = {}
        self.routes = defaultdict(list)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customerHistory[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.customerHistory[id]

        self.routes[(startStation, stationName)].append(t - startTime)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        times = self.routes[(startStation, endStation)]
        return sum(times)/len(times)
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
