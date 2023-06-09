from typing import Deque


class MyStack:
    # using one queue to implement stack
    def __init__(self):
        self.que = Deque()

    def push(self, x: int) -> None:
        self.que.append(x)

    # test if it is empty 
    # move the left one following the back 
    # then pop the left one 
    def pop(self) -> int:
        if self.empty():
            return None
        for i in range(len(self.que) - 1):
            self.que.append(self.que.popleft())
        return self.que.popleft()

    # if not empty, return the last element 
    def top(self) -> int:
        if self.empty():
            return None
        return self.que[-1]

    def empty(self) -> bool:
        return not self.que

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()