class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        """
        Approach:
        - First, sort `nums` and store it in `sorted_list`.
        - Use a dictionary (`dict_`) to map each number to its first occurrence index in `sorted_list`.
        - Iterate through the original `nums` list and replace each number with its corresponding index from `dict_`.

        Why this works:
        - The index in `sorted_list` represents how many numbers are smaller than the current number.
        - Using a dictionary ensures we only store each unique number once, improving efficiency.
        """

        sorted_list = sorted(nums)  # Sort the numbers
        dict_ = {}

        # Create a mapping of each number to its first occurrence index
        for index, value in enumerate(sorted_list):
            if value not in dict_:
                dict_[value] = index

        # Replace each number with its corresponding index from `dict_`
        return_lst = [dict_[num] for num in nums]

        return return_lst


# Example usage
nums = [8, 1, 2, 2, 3]
sol = Solution()
print(sol.smallerNumbersThanCurrent(nums))  # Output: [4, 0, 1, 1, 3]

"""
Workflow:

1. Sort nums: [8, 1, 2, 2, 3] → sorted_list = [1, 2, 2, 3, 8]
2. Create dict_ mapping:
   {1: 0, 2: 1, 3: 3, 8: 4}  # Stores first occurrence index
3. Transform nums:
   nums = [8, 1, 2, 2, 3]
   Output = [4, 0, 1, 1, 3]  # Based on dict_ values

Time Complexity: **O(n log n)**
- Sorting takes **O(n log n)**
- Creating `dict_` takes **O(n)**
- Constructing `return_lst` takes **O(n)**
- Overall: **O(n log n)** due to sorting.

Space Complexity: **O(n)**
- We store `sorted_list`, `dict_`, and `return_lst`.
"""

