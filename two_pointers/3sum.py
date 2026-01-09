"""
Three Sum (3Sum) - Detailed Learning Notes
==========================================

Problem (plain English)
-----------------------
Given a list of integers `nums`, find all unique triplets [a, b, c] such that:
- a + b + c == 0
- The indices of a, b, c are all different
- The triplets are unique (no duplicates)

You can return the triplets in any order.

Core Strategy: Sort + Two Pointers
----------------------------------
If we sort the array first, we can:
1) Fix one number at index i.
2) Use two pointers (l, r) to find pairs on the right side that sum to -nums[i].

This reduces the problem from O(n^3) brute force to O(n^2).

Why sorting helps (the intuition)
---------------------------------
Sorted order gives us two key powers:
- When the sum is too small, we can increase it by moving l to the right.
- When the sum is too large, we can decrease it by moving r to the left.
This monotonic movement is what makes two pointers work.

Handling duplicates (critical!)
-------------------------------
The problem wants unique triplets, so you must skip duplicates:
1) Skip duplicate values for i.
2) After you find a valid triplet, move l and r past any duplicates.

Without these skips, you will collect repeated triplets.

Algorithm walkthrough (high level)
----------------------------------
1) Sort nums.
2) Loop i from 0 to n - 1:
   - If nums[i] is the same as nums[i - 1], skip it (duplicate first element).
   - Set l = i + 1, r = n - 1.
   - While l < r:
       * total = nums[i] + nums[l] + nums[r]
       * If total < 0, move l right.
       * If total > 0, move r left.
       * If total == 0, record triplet, then move both pointers and skip duplicates.

Complexity
----------
- Sorting: O(n log n)
- Outer loop + two pointers: O(n^2)
- Total: O(n^2) time, O(1) extra space (ignoring output)

Common pitfalls
---------------
- Returning duplicate triplets (forgetting to skip duplicates).
- Moving only one pointer after finding a valid triplet.
- Not sorting first (two-pointer logic fails without sorted order).

Interactive skeleton
--------------------
Fill the blanks marked __BLANK__ to complete the solution.
Hints are in the comments near each blank.

Detailed pointer walkthrough (example)
--------------------------------------
Example input:
nums = [-1, 0, 1, 2, -1, -4]

After sorting:
nums = [-4, -1, -1, 0, 1, 2]
 index:  0   1   2  3  4  5

We will show how (i, l, r) move.

Case 1: i = 0 (nums[i] = -4)
- l = 1 (nums[l] = -1), r = 5 (nums[r] = 2)
  total = -4 + -1 + 2 = -3 (too small) -> move l right
- l = 2 (nums[l] = -1), r = 5 (nums[r] = 2)
  total = -4 + -1 + 2 = -3 (too small) -> move l right
- l = 3 (nums[l] = 0),  r = 5 (nums[r] = 2)
  total = -4 + 0 + 2 = -2 (too small) -> move l right
- l = 4 (nums[l] = 1),  r = 5 (nums[r] = 2)
  total = -4 + 1 + 2 = -1 (too small) -> move l right
- l = 5, r = 5 -> stop (l is no longer < r)
Result: no triplet for i = 0

Case 2: i = 1 (nums[i] = -1)
- l = 2 (nums[l] = -1), r = 5 (nums[r] = 2)
  total = -1 + -1 + 2 = 0 -> record [-1, -1, 2]
  move both pointers: l -> 3, r -> 4
  skip duplicates? nums[l] = 0, nums[l-1] = -1 (no)
                  nums[r] = 1, nums[r+1] = 2 (no)
- l = 3 (nums[l] = 0),  r = 4 (nums[r] = 1)
  total = -1 + 0 + 1 = 0 -> record [-1, 0, 1]
  move both pointers: l -> 4, r -> 3
  stop (l is no longer < r)

Case 3: i = 2 (nums[i] = -1)
- nums[i] == nums[i - 1], so skip this i to avoid duplicates.

Final answer: [[-1, -1, 2], [-1, 0, 1]]
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Step 1: sort the array so two pointers work.
        nums.sort()  # Hint: order the array so pointer moves are valid

        res: List[List[int]] = []

        # Cache length to avoid recomputing.
        n = len(nums)  # Hint: cache the length for reuse

        # Step 2: fix the first element of the triplet.
        for i in range(n-1):  # Hint: pick each possible first index (leave room for two numbers)
            # Skip duplicate values for i to avoid repeated triplets.
            if i > 0 and nums[i] == nums[i - 1]:  # Hint: skip repeating the same first value
                continue  # Hint: move to the next i

            # Step 3: two-pointer search for pairs on the right side.
            l, r = i+1, n-1  # Hint: start pointers inside the remaining subarray

            while l < r:
                total = nums[i] + nums[l] + nums[r]  # Hint: sum of the fixed value and both pointers

                if total < 0:
                    l = l+1  # Hint: sum too small -> move left pointer right
                elif total > 0:
                    r = r-1  # Hint: sum too large -> move right pointer left
                else:
                    # Found a valid triplet.
                    res.append([nums[i] , nums[l] , nums[r]])  # Hint: record the current triplet

                    # Move both pointers inward to look for new pairs.
                    l = l+1 # Hint: move left pointer inward after finding a triplet
                    r = r-1  # Hint: move right pointer inward after finding a triplet

                    # Skip duplicates on the left pointer.
                    while l < r and nums[l] == nums[l - 1]:  # Hint: skip any repeated value on the left
                        l = l+1  # Hint: keep moving left while duplicates remain

                    # Skip duplicates on the right pointer.
                    while l < r and nums[r] == nums[r + 1]:  # Hint: skip any repeated value on the right
                        r = r-1  # Hint: keep moving right while duplicates remain

        return res


# Interview-style practice (no solution here):
# You're analyzing daily profit/loss deltas for a product. Find all unique
# combinations of three different days whose deltas sum to a specified target
# (e.g., break-even). Return the triplets of values (not indices), and avoid
# duplicates even if the same delta appears multiple times in the list.
