class MyHashMap:
    # This implementation uses direct addressing:
    # - keys are guaranteed to be in [0, 1_000_000] by the problem
    # - we store values directly in a fixed-size list at index = key
    # - a sentinel value (-1) means "not present"
    #
    # Time complexity:
    # - put/get/remove are all O(1)
    # Space complexity:
    # - O(1_000_001) for the fixed array of possible keys

    def __init__(self):
        # Create an array for every possible key in [0..1_000_000].
        # Start with -1 to mark all keys as absent.
        self.map = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        # Store value directly at the index equal to the key.
        # This overwrites any previous value for that key.
        self.map[key] = value

    def get(self, key: int) -> int:
        # Return the stored value, or -1 if the key is absent.
        return self.map[key]

    def remove(self, key: int) -> None:
        # Reset the slot to -1 to mark the key as absent.
        self.map[key] = -1

# Detailed example walk-through (each "iteration" is one operation):
# Start: map is all -1 (no keys are present)
#
# Operation 1: put(2, 10)
# - map[2] was -1, now set to 10
# - map[2] = 10
#
# Operation 2: get(2)
# - read map[2], which is 10
# - returns 10
#
# Operation 3: get(3)
# - read map[3], which is -1 (never set)
# - returns -1 to indicate "not found"
#
# Operation 4: put(2, 99)
# - overwrite existing value at key 2
# - map[2] changes from 10 to 99
#
# Operation 5: remove(2)
# - set map[2] back to -1
#
# Operation 6: get(2)
# - read map[2], which is now -1
# - returns -1 (key 2 is absent again)
