class MinStack:

    def __init__(self):
        self.arr = []
        

    def push(self, val: int) -> None:
        if self.arr:
            curr_min = self.arr[-1][1]
            if val < curr_min:
                self.arr.append((val, val))
            else:
                self.arr.append((val, curr_min))
        else:
            self.arr.append((val, val))


    def pop(self) -> None:
        self.arr.pop()
        

    def top(self) -> int:
        return self.arr[-1][0]
        

    def getMin(self) -> int:
        return self.arr[-1][1]
        
