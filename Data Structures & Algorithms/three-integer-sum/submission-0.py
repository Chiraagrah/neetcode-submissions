class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for x in range(len(nums)-2):
            if x > 0 and nums[x] == nums[x-1]:
                continue
            if nums[x] > 0:
                break
            star = x+1
            end = len(nums)-1
            while star < end:
                current_sum = nums[x] + nums[star] + nums[end]
                
                if current_sum == 0:
                    ans.append([nums[x], nums[star], nums[end]])
                    star += 1
                    end -= 1
                    while star < end and nums[star] == nums[star - 1]:
                        star += 1
                    while star < end and nums[end] == nums[end + 1]:
                        end -= 1      
                elif current_sum > 0:
                    end -= 1
                else:
                    star += 1
                    
        return ans