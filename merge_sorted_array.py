from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i= m - 1
        j=n-1
        k=m+n-1

        while i>=0 and j>=0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:  # If there are remaining elements in nums2
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        # No need to handle remaining elements in nums1, as they are already in place
# Time Complexity: O(m + n)
# Space Complexity: O(1) since we are modifying nums1 in place
# This function merges two sorted arrays nums1 and nums2 into nums1 in non-decreasing order.