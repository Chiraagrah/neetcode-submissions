class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        temp = sorted(zip(position,speed))
        stck = []
        count = 0
        for x,y in temp:
            y=(target-x)/y
            while stck and stck[-1]<=y:
                stck.pop()
                count-=1   
            count+=1
            stck.append(y)
        return count