def lengthOfLastWord(s: str) -> int:
    return len(s.rstrip().split(' ')[-1]) if s.strip() else 0


# 1. s.strip()
# Removes all leading and trailing spaces.
# If the string is only spaces, s.strip() becomes "" (empty string, which is False in Python).
# That’s why we check if s.strip() — if it’s empty, return 0.
# ✅ Example:
# "   ".strip()   # -> ""
# bool("".strip()) # -> False
# 2. s.rstrip()
# Removes only the trailing spaces (right side).
# This ensures the last "word" is at the end of the string when we split.
# ✅ Example:
# "hello world   ".rstrip()  # -> "hello world"
# 3. .split(' ')
# Splits the string by spaces into a list.
# Example: "hello world".split(' ') → ["hello", "world"].
# If there are multiple spaces, some empty strings ("") may appear in the list.
# ✅ Example:
# "fly   moon".split(' ')  # -> ["fly", "", "", "moon"]
# 4. [-1]
# Picks the last element of the split list.
# After rstrip(), this will always be the last word (not empty).
# ✅ Example:
# "fly   moon  ".rstrip().split(' ')[-1]  # -> "moon"
# 5. len(...)
# Finally, we measure the length of that last word.
# ✅ Example:
# len("moon")  # -> 4
# 🔎 Full Flow Example
# Input:
# s = "   fly me   to   the moon  "
# Step by step:
# s.strip() → "fly me to the moon" (not empty → continue).
# s.rstrip() → " fly me to the moon".
# .split(' ') → ["", "", "", "fly", "me", "", "", "to", "", "", "the", "moon"].
# [-1] → "moon".
# len("moon") → 4.
# Output = 4. ✅