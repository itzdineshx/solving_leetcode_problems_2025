#solution Level: better
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        """
        Approach:
        1. Convert the list into a set (`set(nums)`) to remove duplicate values.
        2. Compare the length of the original list (`len(nums)`) with the length of the set.
        3. If both lengths are equal, it means no duplicates exist → Return `False`.
        4. Otherwise, return `True` (indicating duplicates exist).
        """

        # Base condition for checking duplicate values
        if len(set(nums)) == len(nums):  
            return False
        else:
            return True


# Example usage
nums1 = [1, 1, 1, 3, 3, 4, 3, 2, 4]
sol = Solution()
print(sol.containsDuplicate(nums1))  # Output: True

"""
Time Complexity: O(n)  
    - Creating a set takes O(n) in the worst case.
Space Complexity: O(n)  
    - The set stores up to `n` elements.
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        """
        Optimized Approach:
        - Instead of using an explicit `if` condition, we directly return `len(set(nums)) != len(nums)`.
        - If the lengths are different, duplicates exist → Returns `True`.
        - Otherwise, returns `False`.
        - This makes the code more concise and readable.
        """
        
        return len(set(nums)) != len(nums)


# Example usage
nums1 = [1, 1, 1, 3, 3, 4, 3, 2, 4]
sol = Solution()
print(sol.containsDuplicate(nums1))  # Output: True

"""
Time Complexity: O(n)  
    - Creating a set requires O(n) operations.

Space Complexity: O(n)  
    - In the worst case (if all elements are unique), the set takes O(n) space.
"""
