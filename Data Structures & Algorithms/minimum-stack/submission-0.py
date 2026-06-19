class MinStack:

    def __init__(self):
        self.stack = []
        self.mi = float('inf')
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val<self.mi:
            self.mi=val

    def pop(self) -> None:
        if self.stack:
            te = self.stack.pop()
            if te== self.mi:
                if self.stack:
                    self.mi = min(self.stack)
                else:
                    self.mi = float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mi
        
