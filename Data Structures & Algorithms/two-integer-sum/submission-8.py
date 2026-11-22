class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hushtable = {}
        for index, number in enumerate(nums):
            other = target - number
            if other in hushtable:
                return [hushtable[other],index]
            else:
                hushtable[number] = index
    

            
        
        
        