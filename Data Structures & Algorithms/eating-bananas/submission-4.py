class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        ans = float("inf")
        while start<=end:
            mid = (start+end)//2
            count = 0
            print(mid)
            for x in piles:
                if count>h:
                    break
                elif x < mid:
                    count += 1
                    continue
                elif x%mid == 0:
                    count += x//mid
                else:
                    count += (x//mid) + 1
            if count<=h:
                print(ans,mid)
                ans = min(ans,mid)
                end = mid - 1
            else:
                start = mid + 1
        return ans


        
