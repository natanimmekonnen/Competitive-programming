# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        x  = len(image)
        y= len(image[0])

        for i in range(x):
            image[i].reverse()
            for j in range(y):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0
        
        return image
        