class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        temp = sorted(zip(position,speed),reverse=True)
        stck = []
        count = 0
        for x,y in temp:
            y=(target-x)/y
            if stck and stck[-1]>=y:
                continue
            stck.append(y)
        return len(stck)