
# Import List from typing for type hints
from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""  # Initialize an empty string to store the encoded result

        # Iterate through each string in the input list
        for s in strs:
            # For each string, append its length, a separator '#', and the string itself
            # Example: for s = "abc", len(s) = 3, so we add "3#abc" to res
            res += str(len(s)) + '#' + s

        # After processing all strings, return the encoded string
        return res
    

    def decode(self, s: str) -> List[str]:
        result = []  # List to store the decoded strings
        i = 0  # Pointer to track our position in the encoded string

        # We use a while loop because we don't know in advance how many strings are encoded,
        # and we need to move the pointer i by variable steps depending on the length of each string.
        # A for loop is not suitable because the step size changes dynamically.
        # An if statement is not suitable because we need to process the entire string, not just one condition.
        while i < len(s):
            j = i  # Start another pointer j at i to find the separator '#'
            # Move j forward until we find the '#' character, which separates the length from the string
            while s[j] != '#':
                j += 1

            # The substring from i to j (not including j) is the length of the next string
            length = int(s[i:j])

            # The actual string starts after '#' and is of 'length' characters
            result.append(s[j+1:j+1+length])

            # Move i to the start of the next encoded string segment
            i = j + 1 + length

        # After processing the entire encoded string, return the list of decoded strings
        return result
            