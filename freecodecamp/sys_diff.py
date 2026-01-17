def sym(*arrays):
    # Defines the symmetric-difference function for 2+ arrays.
    # It accepts any number of lists/iterables as positional args.
    # Example: sym([1, 2], [2, 3]) -> [1, 3].
    """
    Return the symmetric difference across two or more arrays.
    Only unique values are returned, in order of first appearance.
    """
    # The docstring above states the function's intent and output rules.
    # It documents unique-only output and stable first-appearance order.
    # Example: [1, 2, 2, 3] with [2, 3, 4] -> [1, 4].
    if len(arrays) < 2:
        # Guard clause: you need at least two arrays to compare.
        # This avoids ambiguous behavior when only one or zero inputs exist.
        # Example: sym([1, 2]) raises ValueError.
        raise ValueError("sym requires at least two arrays")
        # The exception explains why the function cannot proceed.
        # It keeps caller expectations clear and explicit.
        # Example: ValueError shows up if called with one list.

    counts = {}
    # counts maps each value to how many arrays include it at least once.
    # This ignores duplicates within the same array for correct behavior.
    # Example: counts[2] becomes 1 even if array has [2, 2].
    for arr in arrays:
        # Iterate over each input array to tally unique memberships.
        # Each array is processed independently before moving to the next.
        # Example: first arr = [1, 2, 2, 3], second arr = [2, 3, 4].
        seen = set()
        # seen tracks values already counted in the current array.
        # This prevents double-counting duplicates from one array.
        # Example: in [2, 2], only one "2" is counted for that array.
        for val in arr:
            # Walk each element in the current array.
            # Each val is checked against the current-array seen set.
            # Example: val = 2, then val = 2 again on the next iteration.
            if val in seen:
                # Skip if we've already counted this value for this array.
                # This keeps the per-array contribution at most 1 per value.
                # Example: second "2" in [2, 2, 3] is ignored.
                continue
                # Continue jumps to the next val without updating counts.
                # It avoids inflating the membership count incorrectly.
                # Example: duplicate "2" doesn't increase counts[2].
            seen.add(val)
            # Record that this value has been seen in the current array.
            # This ensures duplicates in the same array are ignored later.
            # Example: after val=2, seen becomes {2}.
            counts[val] = counts.get(val, 0) + 1
            # Increment the number of arrays that include this value.
            # counts.get provides 0 for unseen values before incrementing.
            # Example: counts[2] goes 0->1 for first array, 1->2 for second.

    result = []
    # result will store values that appear an odd number of arrays.
    # It preserves the first-appearance order across all arrays.
    # Example: if 1 appears first, it will appear first in result.
    added = set()
    # added tracks which values are already in result to avoid duplicates.
    # This enforces unique output, even if a value appears in many arrays.
    # Example: if 1 qualifies, it is only appended once.
    for arr in arrays:
        # Iterate again to output values in first-appearance order.
        # This pass uses the original ordering of the input arrays.
        # Example: value order from arrays: [1, 2, 2, 3], then [2, 3, 4].
        for val in arr:
            # Walk each element to decide if it should be emitted.
            # Output order is determined by the first time we see a value.
            # Example: value 1 is evaluated before 4, so output starts with 1.
            if val in added:
                # Skip values that are already in the result list.
                # This enforces unique output values exactly once.
                # Example: if 1 already added, subsequent 1s are ignored.
                continue
                # Continue avoids re-adding duplicates to result.
                # It keeps output list free of repeated elements.
                # Example: second occurrence of 4 is skipped.
            if counts.get(val, 0) % 2 == 1:
                # Check if value appears in an odd number of arrays.
                # Odd counts mean the value is in the symmetric difference.
                # Example: counts[1]=1 -> keep, counts[2]=2 -> drop.
                result.append(val)
                # Add the qualifying value to the output list.
                # This preserves the first-appearance order for output.
                # Example: result becomes [1], later [1, 4].
            added.add(val)
            # Mark value as processed for output, regardless of parity.
            # This avoids reconsidering the same value later in the pass.
            # Example: after seeing 2, added includes 2 even if not appended.

    return result
    # Return the final symmetric difference list.
    # Output contains unique values and stable first-appearance order.
    # Example: sym([1, 2, 2, 3], [2, 3, 4]) -> [1, 4].


def sym_set(*arrays):
    # Defines a simpler set-based version of symmetric difference.
    # It trades ordering for simplicity and brevity.
    # Example: sym_set([1, 2], [2, 3]) -> [1, 3] (order varies).
    """
    Simpler symmetric difference using sets.
    Returns unique values; order is not guaranteed.

    Example:
        sym_set([1, 2, 2, 3], [2, 3, 4]) -> [1, 4]  # order may vary
    """
    # The docstring explains the set-based approach and the order caveat.
    # It also includes an example of the expected output.
    # Example: [1, 2, 2, 3] with [2, 3, 4] gives [1, 4] in any order.
    if len(arrays) < 2:
        # Guard clause mirrors sym() to enforce 2+ inputs.
        # This avoids undefined meaning for a single array.
        # Example: sym_set([1, 2]) raises ValueError.
        raise ValueError("sym_set requires at least two arrays")
        # The exception text tells the caller what's required.
        # It prevents silent errors or misleading results.
        # Example: explicit ValueError is easier to debug.

    result = set()
    # result starts as an empty set for XOR accumulation.
    # Set XOR keeps values that appear in an odd number of sets.
    # Example: {} XOR {1,2} -> {1,2}.
    for arr in arrays:
        # Iterate each array and combine with XOR.
        # Each array is converted to a set to remove duplicates.
        # Example: arr=[2,2,3] becomes {2,3} before XOR.
        result ^= set(arr)
        # XOR toggles membership: in once => in, in twice => out.
        # This matches the symmetric difference definition.
        # Example: {1,2,3} XOR {2,3,4} -> {1,4}.

    return list(result)
    # Convert the set to a list for the required return type.
    # Ordering is not stable due to set iteration behavior.
    # Example: list({1,4}) may be [1,4] or [4,1].


SYM_ANALYSIS = """
Detailed analysis with examples

1) sym(*arrays)
- Goal: return values that appear in an odd number of arrays.
- The first pass builds counts per value, but only once per array.
  - The "seen" set avoids counting duplicates within the same array.
- The second pass emits each value once, in first-appearance order.
  - "added" prevents duplicates in the output.

Example A:
  arrays = ([1, 2, 2, 3], [2, 3, 4])
  counts after pass 1:
    1 -> 1, 2 -> 2, 3 -> 2, 4 -> 1
  odd counts: 1 and 4
  output order from pass 2: [1, 4]

Example B:
  arrays = ([1, 2], [2, 3], [3, 1, 1])
  counts after pass 1:
    1 -> 2, 2 -> 2, 3 -> 2
  all even, so output: []

Complexity:
  time: O(n) over total input size
  space: O(u) for unique values

2) sym_set(*arrays)
- Uses set symmetric difference to keep values seen an odd number of times.
- Each array is deduped via set(arr) before XOR.
- Output is a list, but order is not guaranteed.

Example A:
  result starts {}
  XOR with {1, 2, 3} -> {1, 2, 3}
  XOR with {2, 3, 4} -> {1, 4}
"""
# SYM_ANALYSIS is a long-form string that documents the approach.
# It keeps multi-example reasoning in one place for quick reference.
# Example: it explicitly shows how counts lead to [1, 4].
