from collections import Counter  # Import Counter to count occurrences of elements in a list

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # nums: List of integers, e.g., [1,1,1,2,2,3]
        # k: Number of most frequent elements to return, e.g., 2
        # Example: For nums = [1,1,1,2,2,3], k = 2, the answer is [1,2]

        # Counter(nums) creates a dictionary-like object where keys are elements from nums
        # and values are their counts. For example, Counter([1,1,1,2,2,3]) -> {1: 3, 2: 2, 3: 1}
        # .most_common(k) returns a list of the k most common elements and their counts,
        # sorted from most to least frequent. For example, Counter([1,1,1,2,2,3]).most_common(2) -> [(1, 3), (2, 2)]
        # The list comprehension extracts just the numbers from these pairs.
        # So, [number for number, frequency in ...] gives [1, 2] so here 1 is the number and 2 is the frequency
        return [number for number, frequency in Counter(nums).most_common(k)]  # Return the k most frequent elements