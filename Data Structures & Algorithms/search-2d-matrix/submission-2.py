class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start=0
        end=len(matrix)-1
        mid = 0
        while start<=end:
            mid = (end+start)//2
            if target >= matrix[mid][0] and (mid==len(matrix)-1 or target< matrix[mid+1][0]):
                break
            elif target< matrix[mid][0]:
                end=mid-1
            else:
                start=mid+1
        mid2=0
        start=0
        end = len(matrix[0])-1
        while start<=end:
            mid2 = (end+start)//2
            if target==matrix[mid][mid2]:
                return True
            elif target < matrix[mid][mid2]:
                end=mid2-1
            else:
                start=mid2+1
        return False

        