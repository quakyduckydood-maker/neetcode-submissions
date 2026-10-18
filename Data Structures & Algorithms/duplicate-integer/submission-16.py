class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dick = set()
        for number in nums:
            if number in dick:
                return True
            else:
                dick.add(number)
                
        return False
