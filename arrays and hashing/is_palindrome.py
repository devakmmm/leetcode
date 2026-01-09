def solution(self, s: str) -> bool:  # Define the method; e.g., s = "A man, a plan, a canal: Panama"
    cleaned = ""  # Collect only lowercase letters/digits; e.g., becomes "amanaplanacanalpanama"
    for ch in s:  # Walk each character; e.g., ch = "A", then " ", then "m"
        if ch.isalnum():  # Keep letters/digits only; e.g., "A" -> True, " " -> False
            cleaned += ch.lower()  # Append lowercase char; e.g., "A" -> "a", cleaned = "a"
    return cleaned == cleaned[::-1]  # Palindrome check; e.g., "aba" == "aba" -> True
