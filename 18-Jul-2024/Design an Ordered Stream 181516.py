# Problem: Design an Ordered Stream - https://leetcode.com/problems/design-an-ordered-stream/

class OrderedStream:

    def __init__(self, n: int):
        self.n=n
        self.stream=[""]*n
        self.c=0

        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey-1]=value
        if idKey-1>self.c:
            return []
        while self.n > self.c and self.stream[self.c]:
            self.c+=1
        return self.stream[idKey-1:self.c]
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)