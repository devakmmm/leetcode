"""
Container With Most Water - Detailed Learning Notes
===================================================

Problem (plain English)
-----------------------
You are given an array `heights` where each value is the height of a vertical
line at that index. Choose two lines that, together with the x-axis, form a
container that holds the most water. The container's area is:
    area = min(height[left], height[right]) * (right - left)

Key observation (the "bottleneck" idea)
---------------------------------------
The amount of water is limited by the *shorter* of the two lines. That shorter
line is the bottleneck. If you move the taller line inward, the width shrinks,
but the bottleneck does not improve, so the area cannot increase.

So the only move that can *possibly* increase the area is to move the pointer
at the shorter line, hoping to find a taller line that raises the bottleneck.

Two-pointer strategy
--------------------
1) Start with the widest container: left = 0, right = n - 1.
2) Compute the area and track the maximum seen so far.
3) Move the pointer at the shorter line inward.
4) Repeat until the pointers meet.

Why this is safe (intuition you should memorize)
------------------------------------------------
If heights[left] <= heights[right]:
- The current area is limited by heights[left].
- Any container that keeps the same left and moves right inward will have
  smaller width and the same limiting height, so it cannot be better.
- Therefore, we must move left to have a chance at a taller limiting height.
The symmetric argument holds when heights[right] < heights[left].

Complexity
----------
- Time: O(n) because each pointer moves at most n times.
- Space: O(1) extra space.

Common pitfalls
---------------
- Using max(height[left], height[right]) instead of min.
- Moving the taller pointer (this can skip optimal answers).
- Trying all pairs (O(n^2)) when O(n) is possible.

Walkthrough (short example)
---------------------------
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
Start: left=0 (1), right=8 (7)
area = min(1,7) * (8-0) = 8 -> move left (shorter)
left=1 (8), right=8 (7)
area = min(8,7) * 7 = 49 -> move right (shorter)
left=1 (8), right=7 (3)
area = min(8,3) * 6 = 18 -> move right (shorter)
...
Maximum found is 49.
"""

from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            # Compute the area with the current pair.
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            # Move the pointer at the shorter line (the bottleneck).
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res
