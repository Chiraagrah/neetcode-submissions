class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = len(matrix[0])
        left,right = 0, (len(matrix)*col) - 1
        
        while left<=right:
            mid = left + ((right-left)//2)
            num = matrix[mid//col][mid%col]
            if num==target:
                return True
            elif num>target:
                right = mid - 1
            else:
                left = mid + 1 
        return False

        