class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for other in nums[i+1:]:
                if nums[i] == other:
                    return True
        
        return False