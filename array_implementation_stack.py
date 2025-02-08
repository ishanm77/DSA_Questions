class MyStack:
    
    def __init__(self):
        self.arr=[]
    
    #Function to push an integer into the stack.
    def push(self,data):
        self.arr.append(data)
    
    #Function to remove an item from top of the stack.
    def pop(self):
        if not self.arr:
            return -1
        return self.arr.pop()
        
def process_queries(queries):
    arr=arr()
    result=[]
    for query in queries:
        q=query.split()
        if q[0]==1:
            arr.push(int(q[1]))
        elif q[1]==2:
            result.append(arr.pop())
    return result