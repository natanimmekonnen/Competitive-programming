# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.minn = [] 
        self.maxx = []  

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minn, -num)
        
        if self.minn and self.maxx and (-self.minn[0] > self.maxx[0]):
            heapq.heappush(self.maxx, -heapq.heappop(self.minn))
        
        if len(self.minn) > len(self.maxx) + 1:
            heapq.heappush(self.maxx, -heapq.heappop(self.minn))
        if len(self.maxx) > len(self.minn):
            heapq.heappush(self.minn, -heapq.heappop(self.maxx))
        

    def findMedian(self) -> float:
        if len(self.minn) > len(self.maxx):
            return -self.minn[0]
        else:
            return (-self.minn[0] + self.maxx[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()