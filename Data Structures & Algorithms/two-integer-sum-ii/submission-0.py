class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        star = 0
        end= len(numbers)-1
        while star<end:
            if numbers[star] + numbers[end] == target:
                return [star+1,end+1]
            elif numbers[star] + numbers[end] < target:
                star += 1
            elif numbers[star] + numbers[end] > target:
                end -= 1