class MyQueue(object):

    def __init__(self):
        self.mystack = []

    def push(self, x):
        self.mystack.append(x)

    def pop(self):
        ret = self.mystack[0]
        del self.mystack[0]
        return ret

    def peek(self):
        return self.mystack[0]

    def empty(self):
        ret = False if len(self.mystack) else True
        return ret