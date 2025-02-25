class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        """
        Approach:
        - Convert `nums` into a set (`set_list`) to allow O(1) lookups.
        - Initialize an empty list (`return_list`) to store missing numbers.
        - Iterate over the range `1` to `n` (length of `nums`):
            - If a number is not present in `set_list`, add it to `return_list`.
        - Return the final list of missing numbers.
        """

        # Convert nums to a set for quick lookup
        set_list = set(nums)

        # Initialize an empty list for missing numbers
        return_list = []

        # Iterate through numbers from 1 to n
        for num in range(1, len(nums) + 1):
            # If num is missing, append to return_list
            if num not in set_list:
                return_list.append(num)

        return return_list


# Example usage
nums = [4, 3, 2, 7, 8, 2, 3, 1]
sol = Solution()
print(sol.findDisappearedNumbers(nums))  # Output: [5, 6]

"""
Workflow:

1. Convert `nums` into a set (`set_list`) for efficient lookups.
   - Example: nums = [4, 3, 2, 7, 8, 2, 3, 1]
   - set_list = {1, 2, 3, 4, 7, 8}

2. Initialize an empty list `return_list`.

3. Iterate over numbers from 1 to n (n = 8 in this case):
   - 1 is in set_list → Not missing
   - 2 is in set_list → Not missing
   - 3 is in set_list → Not missing
   - 4 is in set_list → Not missing
   - 5 is NOT in set_list → Append to return_list
   - 6 is NOT in set_list → Append to return_list
   - 7 is in set_list → Not missing
   - 8 is in set_list → Not missing

4. Return return_list → [5, 6]

Time Complexity: O(n)
   - Converting `nums` to a set: O(n)
   - Looping through range(1, n+1): O(n)
   - Checking set membership: O(1) per lookup → O(n) total

Space Complexity: O(n)
   - Storing `set_list`: O(n)
   - Storing `return_list`: O(n) in the worst case (if all numbers are missing)
"""
