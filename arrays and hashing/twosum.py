# Two Sum
# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

class Solution:
    def twoSum(self, nums, target):
        mapped = {}

        for i, num in enumerate(nums):
            complement=target-num
            if complement in mapped:
                return [mapped[complement], i]
            mapped[num] = i

# Time Complexity: O(n)
# Space Complexity: O(n)