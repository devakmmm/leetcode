class Solution:
    def isValid(self, s: str) -> bool:
        # Goal: verify every closing bracket matches the most recent unmatched opening bracket.
        #
        # Example walkthrough (s = "([])"):
        # - Start: stack = []
        # - Read '(' -> opening, push -> stack = ['(']
        # - Read '[' -> opening, push -> stack = ['(', '[']
        # - Read ']' -> closing, top is '[', matches -> pop -> stack = ['(']
        # - Read ')' -> closing, top is '(', matches -> pop -> stack = []
        # End: stack empty -> valid
        #
        # Example invalid (s = "([)]"):
        # - Read '(' -> stack = ['(']
        # - Read '[' -> stack = ['(', '[']
        # - Read ')' -> needs '(' but top is '[' -> mismatch -> invalid immediately

        # Map each closing bracket to the opening bracket it must match.
        close_to_open = {")": "(", "]": "[", "}": "{"}

        # Stack holds unmatched opening brackets, in the order we saw them.
        stack = []

        # Scan characters left to right.
        for c in s:
            # If we see a closing bracket...
            if c in close_to_open:
                # ...we must have an opening bracket to match it.
                if stack and stack[-1] == close_to_open[c]:
                    # The top opening bracket matches, so remove it.
                    stack.pop()
                else:
                    # Either stack is empty or top doesn't match -> invalid.
                    return False
            else:
                # Opening bracket: save it to match with a future closing bracket.
                stack.append(c)

        # If stack is empty, all openings were matched; otherwise, invalid.
        return not stack
