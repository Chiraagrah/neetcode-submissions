class KthLargest:
    nums = []
    k = None
    kth = None
    def __init__(self, k: int, nums: List[int]):
        nums.sort()
        self.nums = nums
        self.k = k
        if k<=len(nums):
            self.kth = nums[-k]
    def add(self, val: int) -> int:
        i = 0
        while i < len(self.nums):
            if self.nums[i]<=val:
                i+=1
            else:
                break
        self.nums.insert(i,val)
        if self.k <= len(self.nums):
            self.kth = self.nums[-self.k]
        return self.kth
        
