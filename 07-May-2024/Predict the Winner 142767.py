# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def finder(arr,sc1,sc2,turn):
            if not arr:
                if sc1>=sc2:
                    return "player1"
                return "player2"
            if turn:
                branch1=finder(arr[1:],sc1+arr[0],sc2,False)
                branch2=finder(arr[:-1],sc1+arr[-1],sc2,False)
                if branch1==branch2=="player2":
                    return "player2"
                return "player1"
            else:
                branch1=finder(arr[1:],sc1,sc2+arr[0],True)
                branch2=finder(arr[:-1],sc1,sc2+arr[-1],True)
                if branch1==branch2=="player1":
                    return "player1"
                return "player2"
        if finder(nums,0,0,True)=="player1":
            return True
        return False
   


        