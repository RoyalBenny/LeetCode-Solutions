#Time : O(N)
#Space : O(N)
#recursion
# https://leetcode.com/problems/flood-fill/
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image:
            return []
        self.fillAlgo(image,sr,sc,color, image[sr][sc])
        return image
    
    def fillAlgo(self,image,sr,sc,color,prevColor):
        if sr<0 or sc<0 or sr>= len(image) or sc>= len(image[0]) or image[sr][sc]!= prevColor or image[sr][sc] == color:
            return
        image[sr][sc] = color
        self.fillAlgo(image,sr+1,sc,color,prevColor)
        self.fillAlgo(image,sr-1,sc,color,prevColor)
        self.fillAlgo(image,sr,sc+1,color,prevColor)
        self.fillAlgo(image,sr,sc-1,color,prevColor)
