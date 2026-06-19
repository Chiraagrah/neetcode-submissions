class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stck = []
        ans=[0]*len(temperatures)
        for x,y in enumerate(temperatures):
            if not stck:
                stck.append([x,y])
            if stck[-1][1]<y:
                while stck and stck[-1][-1]<y:
                    temp_x,temp_y = stck.pop()
                    ans[temp_x] = x - temp_x
            stck.append([x,y])
        return ans
        