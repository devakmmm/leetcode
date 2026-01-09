from typing import List  # Import List for type hints on the input array.


class Solution:  # LeetCode expects the solution inside a class named Solution.
    def majorityElement(self, nums: List[int]) -> int:  # Find the element that appears > n//2 times.
        count = {}  # Map each number to how many times it has been seen so far.
        n = len(nums)  # Store the length so we can compare counts against n//2.
        for num in nums:  # Walk through each number in order.
            count[num] = count.get(num, 0) + 1  # Increment this number's frequency.
            if count[num] > n // 2:  # Majority means strictly more than half the list.
                return num  # Return as soon as the majority count is reached.

# Example trace (shows each iteration in order):
# nums = [2, 2, 1, 2, 3, 2, 2], n = 7, threshold = n//2 = 3, need > 3
# i=0, num=2 -> count={2: 1}, 1 > 3? no
# i=1, num=2 -> count={2: 2}, 2 > 3? no
# i=2, num=1 -> count={2: 2, 1: 1}, 1 > 3? no
# i=3, num=2 -> count={2: 3, 1: 1}, 3 > 3? no
# i=4, num=3 -> count={2: 3, 1: 1, 3: 1}, 1 > 3? no
# i=5, num=2 -> count={2: 4, 1: 1, 3: 1}, 4 > 3? yes -> return 2
