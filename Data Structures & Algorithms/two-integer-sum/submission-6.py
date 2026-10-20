class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i, number in enumerate(nums):
            other = target - number
            if other in hashtable:
                return [hashtable[other],i]
            else:
                hashtable[number] = i