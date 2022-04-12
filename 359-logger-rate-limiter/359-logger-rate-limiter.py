class Logger:
    from collections import OrderedDict
    def __init__(self):
        # save last 10 printed messages and its time. ex) 'foo':3
        self.messagetime = OrderedDict() 
        
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.messagetime:
            tc = self.messagetime[message]
            if timestamp - tc >= 10:
                self.messagetime[message] = timestamp
                return True 
            else:
                return False 
        
        else: # message isn't exist in timestamp
            if len(self.messagetime) >= 10:
                self.messagetime.popitem(last=True)
            self.messagetime[message] = timestamp 
            return True 
            

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)