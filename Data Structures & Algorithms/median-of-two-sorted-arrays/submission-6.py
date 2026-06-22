class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array so the binary search range is minimized
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        x, y = len(nums1), len(nums2)
        low, high = 0, x
        
        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX
            
            # If partitionX is 0, nothing is on the left side of nums1. Use -infinity
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            # If partitionX is x, nothing is on the right side of nums1. Use +infinity
            minRightX = float('inf') if partitionX == x else nums1[partitionX]
            
            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == y else nums2[partitionY]
            
            # Check if we found the correct partition
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # If total length is even
                if (x + y) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
                # If total length is odd
                else:
                    return max(maxLeftX, maxLeftY)
                    
            elif maxLeftX > minRightY:
                # We are too far right in nums1, move left
                high = partitionX - 1
            else:
                # We are too far left in nums1, move right
                low = partitionX + 1