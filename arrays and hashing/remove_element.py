from typing import List  # Import List for type hints on the input array.


class Solution:  # LeetCode expects the solution inside a class named Solution.
    def removeElement(self, nums: List[int], val: int) -> int:  # Remove all instances of val in-place.
        k = 0  # Write index for the next kept element (also the count of kept elements).
        n = len(nums)  # Store length so we iterate over the original array once.

        for i in range(n):  # Read index scans every position in the original array.
            if nums[i] != val:  # Keep only elements that are not equal to val.
                nums[k] = nums[i]  # Write the kept value into the next free position.
                k = k + 1  # Advance write index after placing a kept value.

        return k  # Return the number of kept elements (new length).

# Example trace (shows each iteration in order):
# nums = [3, 2, 2, 3, 4], val = 3
# Start: k = 0
# i=0, nums[i]=3 -> equals val, skip; k=0, nums unchanged
# i=1, nums[i]=2 -> keep; write nums[0]=2; k=1; nums=[2, 2, 2, 3, 4]
# i=2, nums[i]=2 -> keep; write nums[1]=2; k=2; nums=[2, 2, 2, 3, 4]
# i=3, nums[i]=3 -> equals val, skip; k=2, nums unchanged
# i=4, nums[i]=4 -> keep; write nums[2]=4; k=3; nums=[2, 2, 4, 3, 4]
# Return k=3, and the first 3 elements of nums are the kept values: [2, 2, 4]
