# This file solves: "Capacity to Ship Packages Within D Days" from LeetCode.  # We say what problem this file explains.
# The goal is to find the smallest ship capacity that can ship all packages in a given number of days.  # Simple goal statement.
# We use binary search because the answer is a number and bigger capacity always makes it easier to ship.  # Explain the key idea.
# Everything is commented like a story so a very young reader can follow each tiny step.  # Explain the teaching style.
from typing import List  # This lets us write List[int] to describe lists of numbers.
# We now define the class that LeetCode expects.  # Explain why this class exists.
class Solution:  # LeetCode calls a method inside this class.
    # This method returns the smallest capacity that works.  # Explain what the method does.
    def shipWithinDays(self, weights: List[int], days: int) -> int:  # We take weights and days, and return an integer.
        # The smallest possible capacity must be at least the heaviest single package.  # You cannot carry less than the biggest weight.
        min_capacity = max(weights)  # This is the lowest capacity we can even consider.
        # The largest possible capacity is the sum of all packages in one day.  # That would ship everything at once.
        max_capacity = sum(weights)  # This is the highest capacity we would ever need.
        # We will search between these two numbers.  # Binary search needs a left and right bound.
        left = min_capacity  # Left edge of the search range.
        right = max_capacity  # Right edge of the search range.
        # We make a helper function to check if a capacity works in the given days.  # This is our "can we do it?" test.
        def can_ship(capacity: int) -> bool:  # The helper returns True if this capacity is enough.
            # Start with day 1 because we have not shipped anything yet.  # We always begin on the first day.
            days_used = 1  # This counts how many days we are already using.
            # Start with an empty ship for the current day.  # The ship begins with zero weight today.
            current_load = 0  # This is how much weight is on the ship right now.
            # We go through each package in order because the problem says we cannot reorder them.  # Order matters.
            for w in weights:  # Look at each package weight, one by one.
                # If the current package fits in today's ship, we add it.  # We keep loading until we hit the limit.
                if current_load + w <= capacity:  # Check if adding this package stays within capacity.
                    current_load += w  # Put this package on today's ship.
                # Otherwise, the package does not fit today, so we start a new day.  # We need another day.
                else:  # This branch runs when the package does not fit today.
                    days_used += 1  # We move to the next day.
                    current_load = w  # The new day starts with this package on the ship.
                    # If we used more days than allowed, this capacity fails.  # Too many days means "no".
                    if days_used > days:  # Check if we already broke the day limit.
                        return False  # This capacity is not enough.
            # If we never broke the day limit, the capacity works.  # We shipped everything in time.
            return True  # The capacity is good enough.
        # Now we do a binary search to find the smallest capacity that works.  # Narrow the range quickly.
        while left < right:  # Keep going until left and right meet at the answer.
            # Pick the middle capacity to test.  # Binary search always tests the middle.
            mid = (left + right) // 2  # Use integer division to get a whole number.
            # If the middle capacity works, we try smaller ones.  # We want the minimum working capacity.
            if can_ship(mid):  # Ask the helper if this capacity can ship in time.
                right = mid  # Keep the working capacity, but move the right edge left.
            # If the middle capacity does not work, we need a bigger one.  # We must increase capacity.
            else:  # This branch is for capacity that is too small.
                left = mid + 1  # Move the left edge up past mid.
        # When the loop ends, left == right and it is the smallest working capacity.  # The answer is found.
        return left  # Return the minimum capacity.
        # End of the main solution.  # Marks the end of the method.
# The following block is just a small demo so you can see the idea in action.  # This is for learning only.
# It runs only when this file is run directly, not on LeetCode.  # LeetCode ignores this block.
if __name__ == "__main__":  # Python runs this block only when the file is executed directly.
    # Example input from the problem statement style.  # We pick a simple list of weights.
    example_weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Ten packages in order.
    # Example number of days to ship all packages.  # We want to finish in 5 days.
    example_days = 5  # The day limit for this example.
    # Create a Solution object so we can call the method.  # This matches how LeetCode calls it.
    solver = Solution()  # Make the helper object.
    # Compute the answer using our method.  # This runs the binary search.
    answer = solver.shipWithinDays(example_weights, example_days)  # Get the smallest capacity.
    # Print the answer so we can see it.  # This is just for demonstration in a terminal.
    print("Minimum capacity:", answer)  # Expected output for this example is 15.
    # We now add a tiny, step-by-step story in comments.  # This helps a very young reader.
    # Imagine you have a toy boat that can hold only a little weight each day.  # Child-friendly picture.
    # If the boat is too small, you need too many days.  # This matches the "too many days" rule.
    # If the boat is huge, you can ship everything fast, but that is more than needed.  # We want the smallest big-enough boat.
    # Binary search is like guessing the size in the middle, then saying "too small" or "big enough."  # Simple explanation.
    # We keep guessing until we find the smallest size that still works.  # That smallest size is our answer.
