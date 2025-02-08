class MyQueue:
    def __init__(self):
        self.queue=[]
    #Fu nction to push an element x in a queue.
    def push(self, x):
        self.queue.append(x)
         #add code here
     
    #Function to pop an element from queue and return that element.
    def pop(self): 
        if not self.queue:
            return -1
        return self.queue.pop(0)
        
def process_queries(queries):
    queue = queue()
    result = []
    
    for query in queries:
        q = query.split()
        if q[0] == '1':  # Push operation
            queue.push(int(q[1]))
        elif q[1] == '2':  # Pop operation
            result.append(queue.pop())
    
    return result