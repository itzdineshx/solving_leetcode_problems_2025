class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        Given an array of positive integers and a target sum, this function returns the minimal length 
        of a contiguous subarray of which the sum is greater than or equal to the target. If no such 
        subarray exists, return 0.
        
        :type target: int
        :type nums: List[int]
        :rtype: int
        
        Approach:
        - Use the sliding window technique.
        - Expand the window by moving the right pointer and accumulate the sum.
        - When the sum is greater than or equal to target, shrink the window from the left to find 
          the minimal length subarray that meets the condition.
        - Keep track of the minimum length encountered.
        
        Time Complexity: O(n) - Each element is processed at most twice.
        Space Complexity: O(1) - Uses constant extra space.
        """
        n = len(nums)
        left = 0
        curr_sum = 0
        min_len = float('inf')
        
        for right in range(n):
            curr_sum += nums[right]
            
            # While current window meets or exceeds target, try to shrink it from the left
            while curr_sum >= target:
                min_len = min(min_len, right - left + 1)
                curr_sum -= nums[left]
                left += 1
        
        return 0 if min_len == float('inf') else min_len


"""
Workflow:
1. Initialize left pointer (left = 0), current sum (curr_sum = 0), and minimum length (min_len = infinity).
2. Iterate through the array with right pointer:
   - Add nums[right] to curr_sum.
   - When curr_sum >= target, update min_len with the current window size (right - left + 1).
   - Then shrink the window from the left by subtracting nums[left] from curr_sum and incrementing left.
3. After processing, if min_len was updated, return it; otherwise, return 0.

Example:
- target = 7, nums = [2,3,1,2,4,3]
  - One possible minimal subarray is [4,3] with length 2.
  
Time Complexity: O(n)  
Space Complexity: O(1)
"""
