class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        store = {}
        
        for i, n in enumerate(nums):
            diff = target - n 
            
            if diff in store:
                return [store[diff], i]  
            store[n] = i