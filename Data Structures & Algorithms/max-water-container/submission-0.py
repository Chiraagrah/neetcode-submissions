class Solution:
    def area(self,a,b,left,right):
        height = min(left,right)
        return (b-a)*height

    def maxArea(self, heights: List[int]) -> int:
        a = 0
        b = len(heights)-1
        are = 0
        while a<b and b<len(heights):
            cur = self.area(a,b,heights[a],heights[b])
            if heights[a]>=heights[b] and cur<are:
                b -= 1
            elif heights[a]>=heights[b] and cur>=are:
                are = cur
                b-=1 
            elif heights[a]<heights[b] and cur<are:
                a+=1
            elif heights[a]<heights[b] and cur>=are:
                are = cur
                a+=1
        return are

            
