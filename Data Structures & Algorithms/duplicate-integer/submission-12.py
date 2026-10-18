class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dick = set()
        for i in nums:
            dick.add(i)
        if len(dick) == len(nums):
            return False
        else: 
            return True

