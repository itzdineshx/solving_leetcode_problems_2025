class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        Approach:
        1. First, sort the given list to arrange numbers in ascending order.
        2. Iterate through the sorted list using `enumerate()` to get both index and value.
        3. Check if the index does not match the value:
            - If `index != value`, return `value - 1` (since the missing number should be at this position).
        4. If the loop completes and the last value is equal to `len(nums) - 1`, return `value + 1`.
        
        Edge Cases:
        - If the missing number is at the start or end of the sequence.
        - If `nums` contains only one element.
        """

        nums.sort()  # Sort the list

        for index, value in enumerate(nums):  # Iterate through index and value pairs
            if index != value:
                return value - 1  # Return the missing number

        return nums[-1] + 1  # Handle case where the missing number is at the end


# Example usage
nums1 = [3, 0, 1]
sol = Solution()
print(sol.missingNumber(nums1))  # Output: 2

# Workflow:
"""
Sorted list: [0, 1, 3]

Iteration:
Index  Value
0      0   ✅ (Index matches value)
1      1   ✅ (Index matches value)
2      3   ❌ (Index 2 ≠ Value 3) → Return 3 - 1 = 2

Output: 2
Time Complexity: O(n log n) (due to sorting)  
Space Complexity: O(1) (modifies input list in-place)
"""
