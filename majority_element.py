class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        
        for num in nums:
            if count==0:
                candidate=nums
            count += (1 if num == candidate else -1)
        
        return candidate
# Time Complexity: O(n)
# Space Complexity: O(1) since we are using constant space
# This function finds the majority element in an array, which is the element that appears more than n/2 times.
# It uses the Boyer-Moore Voting Algorithm to achieve this efficiently.
from typing import List 


# or count={}

# for num in nums:
#     count[num] = count.get(num, 0) + 1
#     if count[num] > len(nums) // 2: 
#         return num 
#