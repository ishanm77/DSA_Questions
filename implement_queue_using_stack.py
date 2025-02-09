class MyQueue(object):
# s1=stack1 and s2=stack2
    def __init__(self):
        self.s1=[]
        self.s2=[]

    def push(self, x):
        self.s1.append(x)
        

    def pop(self):
        for i in range(len(self.s1)):
            self.s2.append(self.s1.pop(-1))
        popped=self.s2.pop(-1)
        for i in range(len(self.s2)):
            self.s1.append(self.s2.pop(-1))
        return popped

    def peek(self):
        for i in range(len(self.s1)):
            self.s2.append(self.s1.pop(-1))
        peeked=self.s2[-1]
        for i in range(len(self.s2)):
            self.s1.append(self.s2.pop(-1))
        return peeked
        