# Problem: Convert the Temperature - https://leetcode.com/problems/convert-the-temperature/

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        temp=[0,0]
        temp[0]=celsius+273.15
        temp[1]=celsius*1.80+32.00
        return temp
        