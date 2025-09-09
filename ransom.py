class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_count = {}
        for c in magazine:
            mag_count[c] = mag_count.get(c, 0) + 1

        for c in ransomNote:
            if mag_count.get(c, 0) == 0:
                return False
            mag_count[c] -= 1
        return True
        # Create a dictionary to count the frequency of each character in the magazine
        # Iterate through each character in the ransom note
        # Check if the character is available in the magazine dictionary with a count greater than 0            