class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stck = []
        ans = 0
        dic={}
        dic2={}
        heights = [float("-inf")]+heights+[float("-inf")]
        for ind, hei in enumerate(heights):
            while stck and heights[stck[-1]]>hei:
                temp = stck.pop()
                dic[temp] = ind
            stck.append(ind)
        while stck:
            temp = stck.pop()
            dic[temp]=len(heights)-1
        for ind in range(len(heights)-1,-1,-1):
            while stck and heights[stck[-1]]>heights[ind]:
                temp = stck.pop()
                dic2[temp] = ind
            stck.append(ind)
        while stck:
            temp = stck.pop()
            dic2[temp]=0
        for ind , hei in enumerate(heights):
            ans = max(hei * (dic[ind]-dic2[ind]-1),ans)
        print(dic,dic2)
        return ans
