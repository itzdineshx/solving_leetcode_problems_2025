class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        """
        Approach:
        - Merge the two sorted arrays using `nums1 + nums2`.
        - Sort the merged array.
        - Find the median:
            - If the length (`n`) of the merged array is even, return the average of the two middle values.
            - If `n` is odd, return the middle element directly.
        """

        merged = sorted(nums1 + nums2)  # Merge and sort the arrays
        n = len(merged)

        if n % 2 == 0:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2.0  # Average of middle elements
        else:
            return merged[n // 2]  # Middle element


# Example usage
nums1 = [1, 3]
nums2 = [2]
sol = Solution()
print(sol.findMedianSortedArrays(nums1, nums2))  # Output: 2.0


"""
Workflow:
1. Merge `nums1` and `nums2` using `nums1 + nums2`.
    - Example: nums1 = [1, 3], nums2 = [2]
    - Merged: [1, 3] + [2] → [1, 3, 2]

2. Sort the merged array.
    - Before Sorting: [1, 3, 2]
    - After Sorting: [1, 2, 3]

3. Find the median based on the length (`n`) of the merged list.
    - If `n` is odd: Return the middle element.
        - Example: [1, 2, 3] → Middle element = 2
    - If `n` is even: Return the average of the two middle elements.
        - Example: [1, 2, 3, 4] → (2 + 3) / 2 = 2.5

4. Return the median value.
"""

"""
Time Complexity: O((m + n) log(m + n))
    - `nums1 + nums2` takes O(m + n)
    - Sorting the merged list takes O((m + n) log(m + n))

Space Complexity: O(m + n)
    - The merged array is stored in additional space.
"""

