class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start=0
        end=len(nums)-1
        while start<=end:
            mid = (end+start)//2
            if nums[mid]==target:
                return mid
            elif nums[mid] > target:
                end = mid-1
                continue
            else:
                start=mid+1
                continue
        return -1
