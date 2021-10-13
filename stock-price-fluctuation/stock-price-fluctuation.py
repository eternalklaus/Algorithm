class StockPrice:

    def __init__(self):
        self.timeprice = {}
        self.minheap = []
        self.maxheap = []
        self.currenttime = -1
        
    def update(self, timestamp: int, price: int) -> None:
        self.timeprice[timestamp] = price
        self.currenttime = max(self.currenttime, timestamp)
        heappush(self.maxheap, (-price, timestamp))
        heappush(self.minheap, (price, timestamp))

    def current(self) -> int:
        return self.timeprice[self.currenttime]

    def maximum(self) -> int:
        while True:
            (price, timestamp) = heappop(self.maxheap)
            if self.timeprice[timestamp] == -price: break
        heappush(self.maxheap, (price, timestamp))
        return -price

    def minimum(self) -> int:
        while True:
            (price, timestamp) = heappop(self.minheap)
            if self.timeprice[timestamp] == price: break
        heappush(self.minheap, (price, timestamp))
        return price


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()