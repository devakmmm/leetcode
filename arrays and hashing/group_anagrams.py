class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups=defaultdict(list)

        for s in strs:
            key=''.join(sorted(s)) #what this line does is adds each string after sorting it to the key example: "eat" becomes "aet"
            groups[key].append(s) #this line appends the original string to the list of anagrams corresponding to the sorted key example: "eat" is appended to the list for key "aet"

            ## groups["".join(sorted(s))].append(s) #this line does the same as above in a single line so basically we are addeing sorted words as key and orignal words that are anagrams ie that mean the same as key to the list of that key as values
        
        return list(groups.values())
    # the above program groups anagrams together from a list of strings
# Time Complexity: O(n * k log k) where n is the number of strings and k is the maximum length of a string.
# Space Complexity: O(n) for storing the grouped anagrams.
# It uses a dictionary to map sorted string keys to lists of anagrams.# This function groups anagrams from a list of strings by sorting each string and using the sorted string as a key in a dictionary.
from collections import defaultdict
from typing import List