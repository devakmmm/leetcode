# #Valid Anagram
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
# Time Complexity: O(n)
# Space Complexity: O(n)

# sort and compare method
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t) #since sorted returns a list if both are same then they are anagrams
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(1) if we ignore the space used by the sorting algorithm
