class Solution:
    def area(self,a,b,left,right):
        height = min(left,right)
        return (b-a)*height

    def maxArea(self, heights: List[int]) -> int:
        a = 0
        b = len(heights)-1
        are = 0
        while a<b:
            cur = self.area(a,b,heights[a],heights[b])
            if heights[a]>=heights[b]:
                b -= 1
            else:
                a+=1
            are=max(cur,are)
        return are

            
