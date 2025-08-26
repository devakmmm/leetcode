class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        k = 1
        for i in range(1, len(nums)):
            if nums[i]!=nums[i-1]:
                nums[k] = nums[i]
                k += 1
        
        return k
# Time Complexity: O(n)
# Space Complexity: O(1) since we are modifying nums in place
# This function removes duplicates from a sorted array in-place and returns the new length of the array without duplicates.
# The first k elements of nums will contain the unique elements.
from typing import List

