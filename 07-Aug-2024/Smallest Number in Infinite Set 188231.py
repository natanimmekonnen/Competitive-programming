# Problem: Smallest Number in Infinite Set - https://leetcode.com/problems/smallest-number-in-infinite-set/description/

class SmallestInfiniteSet:

    def __init__(self):
        self.array=list(range(1,1001))
        heapq.heapify(self.array)
        

    def popSmallest(self) -> int:
        return heapq.heappop(self.array)
        

    def addBack(self, num: int) -> None:
        if num not in self.array:
            heapq.heappush(self.array,num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)