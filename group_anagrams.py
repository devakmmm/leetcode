class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups=defaultdict(list)

        for s in strs:
            key=''.join(sorted(s))
            groups[key].append(s)
        
        return list(groups.values())
    # the above program groups anagrams together from a list of strings
# Time Complexity: O(n * k log k) where n is the number of strings and k is the maximum length of a string.
# Space Complexity: O(n) for storing the grouped anagrams.
# It uses a dictionary to map sorted string keys to lists of anagrams.# This function groups anagrams from a list of strings by sorting each string and using the sorted string as a key in a dictionary.
from collections import defaultdict
from typing import List