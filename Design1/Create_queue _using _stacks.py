class MyQueue:

    def __init__(self):
        self.instack=[] # creating instack for input
        self.outstack=[] # creating outstack for popping the elements(FIFO operation)

    def push(self, x):
        self.instack.append(x) # appending input in instack

    def pop(self):
        temp = self.peek() # peeking the last element and storing it in temp
        self.outstack = self.outstack[:-1] # storing values in outstack except the last element
        return temp # returning temp value

    def peek(self):
        if len(self.outstack) == 0: # if outstack is empty
            while self.instack: # while instack is true
                ele = self.instack.pop() # popping elements from instack and storing in 'ele' variable
                self.outstack.append(ele) # insert elements in outstack
        return self.outstack[-1] # returning the last element from outstack

    def empty(self):
        return len(self.instack) + len(self.outstack) == 0 # return true if both instack and outstack is empty


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()