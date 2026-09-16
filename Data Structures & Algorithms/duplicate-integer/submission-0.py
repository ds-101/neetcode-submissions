class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        size = len(nums)-1

        for i in range(size):
            if nums[i]==nums[i+1]:
                return True
        return False
        