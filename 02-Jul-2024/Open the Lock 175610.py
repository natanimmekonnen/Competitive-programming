# Problem: Open the Lock - https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        nums=[]
        adjecentList=defaultdict(list)
        dead=set(deadends)
        queue=deque([("0000",0)])
        visited=set()
        for i in range(10000):
            arr="0000"+str(i)
            nums.append(arr[-4:])
        for arr in nums:
            for i in range(4):
                for digit in [((int(arr[i])+1)%10),((int(arr[i])-1)%10)]:
                    x=arr[:i]+str(digit)+arr[i+1:]
                    if x not in deadends:
                        adjecentList[arr].append(x)
        if "0000" in deadends:return -1
    
        while queue:
            arr,step=queue.popleft()
            if arr==target:
                return step
            for i in adjecentList[arr]:
                if i not in visited:
                    visited.add(i)
                    queue.append((i,step+1))


        return -1