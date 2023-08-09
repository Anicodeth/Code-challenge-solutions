class MedianFinder:

    def __init__(self):
        self.sorted_list = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.sorted_list, num)

    def findMedian(self) -> float:
        length = len(self.sorted_list)
        if length % 2 == 0:
            mid_right = length // 2
            mid_left = mid_right - 1
            return (self.sorted_list[mid_left] + self.sorted_list[mid_right]) / 2
        else:
            mid = length // 2
            return self.sorted_list[mid]
        
