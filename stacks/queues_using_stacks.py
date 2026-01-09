class MyQueue:  # Queue implemented with two stacks; e.g., push 1,2 then pop -> 1 (FIFO)
    def __init__(self):  # Initialize two stacks; e.g., s1=[], s2=[]
        self.s1 = []  # Stack for pushes; e.g., after push(1), s1=[1]
        self.s2 = []  # Stack for pops/peeks; e.g., after transfer, s2=[1]

    def push(self, x: int) -> None:  # Enqueue x; e.g., push(3) adds 3 to the back
        self.s1.append(x)  # Push onto s1; e.g., s1=[1,2] -> [1,2,3]

    def pop(self) -> int:  # Dequeue and return front; e.g., queue [1,2,3] -> returns 1
        if not self.s2:  # If s2 is empty, move items so oldest is on top
            while self.s1:  # Transfer all items from s1 to s2; e.g., s1=[1,2,3]
                self.s2.append(self.s1.pop())  # Pop from s1 to s2; result s2=[3,2,1]
        return self.s2.pop()  # Pop from s2 gives front; e.g., returns 1, s2=[3,2]

    def peek(self) -> int:  # Return front without removing; e.g., queue [1,2] -> returns 1
        if not self.s2:  # If s2 is empty, transfer to expose front
            while self.s1:  # Move all items; e.g., s1=[1,2] -> s2=[2,1]
                self.s2.append(self.s1.pop())  # Transfer each; ensures oldest is on top
        return self.s2[-1]  # Look at top of s2 (front of queue); e.g., 1

    def empty(self) -> bool:  # Check if queue has no elements; e.g., [] -> True
        return not self.s1 and not self.s2  # Empty when both stacks empty; e.g., s1=[], s2=[]
