class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stck = []
        ans = 0
        for ind, hei in enumerate(heights):
            strt = ind
            while stck and stck[-1][-1]>hei:
                strt, pop_hei = stck.pop()
                ans = max(ans,(ind-strt)*pop_hei)
                
            stck.append([strt,hei])
        while stck:
            ans= max(ans,(len(heights)-stck[-1][0])*stck.pop()[1])
        return ans
