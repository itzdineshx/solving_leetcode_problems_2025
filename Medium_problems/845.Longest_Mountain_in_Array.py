class Solution(object):
    def longestMountain(self, arr):
        """
        Finds the length of the longest mountain in an array.
        
        A mountain is defined as a sequence of at least three elements where:
        - There exists an increasing sequence (strictly ascending).
        - Followed by a decreasing sequence (strictly descending).
        
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        if n < 3:
            return 0  # A mountain must have at least 3 elements
        
        longest = 0

        # Iterate through the array to find peaks
        for i in range(1, n - 1):  # A peak can't be at index 0 or n-1
            if arr[i - 1] < arr[i] > arr[i + 1]:  # Identifying a peak
                left, right = i, i

                # Expanding left while in a strictly increasing sequence
                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1

                # Expanding right while in a strictly decreasing sequence
                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1

                # Compute the mountain length
                mountain_length = right - left + 1
                longest = max(longest, mountain_length)

        return longest  # Return the longest mountain found

"""
Workflow:
1. Check if the array has at least 3 elements; otherwise, return 0.
2. Iterate through the array looking for peaks (an element greater than its neighbors).
3. Expand left to find the start of the increasing sequence.
4. Expand right to find the end of the decreasing sequence.
5. Calculate the mountain's length and update the maximum found.
6. Return the longest mountain found.

Time Complexity: O(n) (Each element is processed at most twice)
Space Complexity: O(1) (Only a few extra variables are used)
"""
