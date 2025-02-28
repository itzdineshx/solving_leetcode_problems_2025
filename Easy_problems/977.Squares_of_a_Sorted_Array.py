class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        """
        Approach:
        - Square each element of the array.
        - Sort the squared values (since negative numbers become positive).
        - Return the sorted list.

        Time Complexity: O(n log n) (Sorting takes O(n log n), squaring takes O(n))
        Space Complexity: O(n) (Storing squared values)
        """

        squared_sort = [num**2 for num in nums]  # Step 1: Square all elements
        squared_sort.sort()  # Step 2: Sort the squared values
        return squared_sort  # Step 3: Return the sorted list


# Example usage
nums = [-4, -1, 0, 3, 10]
sol = Solution()
print(sol.sortedSquares(nums))  
# Output: [0, 1, 9, 16, 100]
