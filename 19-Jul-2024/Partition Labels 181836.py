# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n=[0]*26
        dictionr={}
        for i in range(len(s)):
            dictionr[s[i]]=i
        print(dictionr)
        print(len(s))
        ans=[]
        start=0
        end=0
        for i in range (len(s)):
            end=max(end,dictionr[s[i]])
            if i==end:
                ans.append(i-start+1)
                start=i+1
        return ans
        