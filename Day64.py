class MyStack:

    def __init__(self):
        self.stack=[]

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        lth=len(self.stack)
        val=self.stack[lth-1]
        self.stack=self.stack[0:lth-1]
        return val

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def empty(self) -> bool:
        if len(self.stack)==0:return True
