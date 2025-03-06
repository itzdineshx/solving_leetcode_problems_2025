class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        Given an array of distinct integers, returns a list of all pairs of elements with the minimum absolute difference.
        
        :type arr: List[int]
        :rtype: List[List[int]]
        
        Approach:
        1. Sort the array in ascending order.
        2. Traverse the sorted array to determine the minimum absolute difference between adjacent elements.
        3. Traverse the sorted array again to collect all pairs of adjacent elements that have the minimum absolute difference.
        
        This ensures that the pairs returned are in ascending order and contain the smallest difference.
        
        Time Complexity: O(n log n) due to sorting, with additional O(n) for scanning the array.
        Space Complexity: O(n) for storing the output list.
        """
        # Sort the array to bring closer numbers together
        arr.sort()
        
        # Find the minimum difference between adjacent elements
        min_diff = float("inf")
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            if diff < min_diff:
                min_diff = diff
        
        # Collect all pairs with the minimum difference
        result = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] == min_diff:
                result.append([arr[i - 1], arr[i]])
                
        return result


"""
Workflow:
1. Sort the input array.
2. Initialize min_diff to infinity.
3. Iterate through the sorted array:
   - Compute the difference between consecutive elements.
   - Update min_diff if a smaller difference is found.
4. Iterate again through the sorted array:
   - For each consecutive pair, if the difference equals min_diff, add the pair to the result.
5. Return the result list.

Example:
Input: arr = [4, 2, 1, 3]
After sorting: [1, 2, 3, 4]
Minimum difference: 1 (found between all adjacent pairs)
Output: [[1, 2], [2, 3], [3, 4]]

Time Complexity: O(n log n) (sorting dominates)
Space Complexity: O(n)
"""
