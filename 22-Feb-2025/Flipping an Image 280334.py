# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i] = image[i][::-1]
        
        for i in range(len(image)):
            image[i] = [ 0 if i == 1 else 1 for i in image[i]]
        return image
        