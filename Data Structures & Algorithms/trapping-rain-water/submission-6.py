class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right  = len(height) - 1
        lefth = height[left]
        righth = height[right]
        area = 0
        while left < right:
            if height[left]<height[right]:
                left+=1
                lefth = max(lefth,height[left])
                area += lefth - height[left]
            else:
                right -= 1
                righth = max(righth,height[right])
                area += righth - height[right]
        return area
        