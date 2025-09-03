from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if not nums:
            return 0

        k=k%len(nums)
        nums[:] = nums[-k:] + nums[:-k] 