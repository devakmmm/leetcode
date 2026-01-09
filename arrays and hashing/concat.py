from typing import List  # Type hints; e.g., nums: List[int] like [1, 2, 1]


class Solution:  # LeetCode-style class wrapper; e.g., Solution().getConcatenation([1,2,1])
    def getConcatenation(self, nums: List[int]) -> List[int]:  # Return nums + nums; e.g., [1,2,1] -> [1,2,1,1,2,1]
        ans = []  # Output list we build; starts empty: []
        for _ in range(2):  # Loop twice to duplicate the list; iterations: 0 then 1
            for num in nums:  # Walk each value in nums; e.g., 1, then 2, then 1
                ans.append(num)  # Append each value; e.g., [] -> [1] -> [1,2] -> [1,2,1] -> [1,2,1,1,2,1]
        return ans  # Final concatenated list; e.g., [1,2,1,1,2,1]
