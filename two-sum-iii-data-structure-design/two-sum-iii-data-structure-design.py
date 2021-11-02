class TwoSum:

    def __init__(self):
        self.addvals = set()
        self.numbers = set()
        
    def add(self, number: int) -> None:
        # add all possible add values
        if number in self.numbers:
            self.addvals.add(number + number)
        else:
            for n in self.numbers:
                self.addvals.add(n + number)
            self.numbers.add(number)
        
    def find(self, value: int) -> bool:
        if value in self.addvals: return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)