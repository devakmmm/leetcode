# #Valid Anagram
# Given two strings s and t, return true if the two strings are anagrams of each other,
# otherwise return false.

# An anagram is a string that contains the exact same characters as another string,
# but the order of the characters can be different.
#
# Example walkthrough (Counter approach):
# s = "anagram", t = "nagaram"
# Counter(s) -> {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
# Counter(t) -> {'n': 1, 'a': 3, 'g': 1, 'a': 3, 'r': 1, 'm': 1} -> same counts
# Result: True
#
# Example (not anagrams):
# s = "rat", t = "car"
# Counter(s) -> {'r': 1, 'a': 1, 't': 1}
# Counter(t) -> {'c': 1, 'a': 1, 'r': 1} -> different counts
# Result: False

from collections import Counter  # Import Counter to count character frequencies efficiently.


class Solution:
    # LeetCode expects a class named Solution with the target method defined.
    def isAnagram(self, s: str, t: str) -> bool:
        # Build frequency tables for both strings and compare them.
        # If every character has the same count, the strings are anagrams.
        return Counter(s) == Counter(t)
# Time Complexity: O(n)
# Space Complexity: O(n)

# Sort and compare method (alternative approach).
# Note: In a single Python file, redefining class Solution will override the earlier one.
class Solution:
    # This approach sorts both strings and compares the sorted lists of characters.
    def isAnagram(self, s: str, t: str) -> bool:
        # sorted(s) returns a list of characters in ascending order.
        # If the sorted lists match, the strings are anagrams.
        return sorted(s) == sorted(t)
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(1) if we ignore the space used by the sorting algorithm
