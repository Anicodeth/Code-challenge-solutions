class StockSpanner:

    def __init__(self):
        self.prices = []
        self.spans = []

    def next(self, price: int) -> int:
        span = 1
        while self.prices and self.prices[-1] <= price:
            self.prices.pop()
            span += self.spans.pop()
        self.prices.append(price)
        self.spans.append(span)
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
