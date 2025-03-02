from collections import defaultdict

class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """

        """
        Approach:
        - Use a dictionary (`defaultdict(int)`) to store the sum of values for each unique index.
        - Traverse `nums1` and add its index-value pairs to the dictionary.
        - Traverse `nums2` and add its index-value pairs to the dictionary.
        - Convert the dictionary back into a sorted list format to maintain order.
        """

        merged_dict = defaultdict(int)  # Dictionary to store index-value pairs
        
        # Add elements from nums1
        for index, value in nums1:
            merged_dict[index] += value
        
        # Add elements from nums2
        for index, value in nums2:
            merged_dict[index] += value
        
        # Convert dictionary back to sorted list format
        return sorted(merged_dict.items())


# Example usage
nums1 = [[1, 2], [2, 3], [4, 5]]
nums2 = [[1, 3], [3, 4], [4, 2]]
sol = Solution()
print(sol.mergeArrays(nums1, nums2))  # Output: [[1, 5], [2, 3], [3, 4], [4, 7]]

"""
Workflow:
1. Initialize a `defaultdict(int)` to store cumulative sums for each index.
2. Iterate over `nums1` and `nums2`, updating the dictionary accordingly.
3. Convert the dictionary back to a sorted list format.
4. Return the sorted merged list.

Time Complexity: O((m + n) log(m + n))
    - Traversing `nums1` and `nums2` takes O(m + n).
    - Sorting the dictionary keys takes O((m + n) log(m + n)).

Space Complexity: O(m + n)
    - The dictionary stores up to `m + n` unique indices.
"""
