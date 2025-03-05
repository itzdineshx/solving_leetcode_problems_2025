class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        Checks if there are any duplicate values in the array such that the indices of the duplicate values are at most k apart.

        :type nums: List[int]
        :type k: int
        :rtype: bool

        Approach:
        - Iterate through the list of numbers while maintaining a dictionary to store the most recent index of each number.
        - For each number:
            1. If the number exists in the dictionary and the difference between the current index and its last seen index is less than or equal to k, return True.
            2. Otherwise, update the dictionary with the current index.
        - If no such duplicate pair is found after processing the list, return False.

        Time Complexity: O(n)
            - We traverse the list once.
        Space Complexity: O(n)
            - In the worst case, the dictionary stores every element in the list.
        """
        last_seen = {}  # Dictionary to store the last seen index for each number

        for i, num in enumerate(nums):
            if num in last_seen and i - last_seen[num] <= k:
                return True
            last_seen[num] = i

        return False


# Example usage:
nums = [1, 2, 3, 1]
k = 3
sol = Solution()
print(sol.containsNearbyDuplicate(nums, k))  # Output: True

"""
Workflow:
1. Initialize an empty dictionary called `last_seen`.
2. Iterate through the list `nums` with both index and value.
   - For each number, check if it exists in `last_seen` and if the current index minus the stored index is less than or equal to k.
   - If such a condition is met, return True immediately.
   - Otherwise, update the dictionary with the current index for that number.
3. If the loop completes without finding any valid duplicates, return False.
"""
