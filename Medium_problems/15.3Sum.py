class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        """
        Approach:
        - Sort the array to make duplicate detection easier.
        - Iterate through each number `nums[i]`, treating it as the first number in the triplet.
        - Use two-pointer approach to find the remaining two numbers.
        - If `nums[i] > 0`, break early since no three positive numbers can sum to zero.
        - Skip duplicate values to avoid duplicate triplets.

        Time Complexity: O(n^2) (Sorting: O(n log n) + Two-pointer traversal: O(n^2))
        Space Complexity: O(1) (In-place sorting, output storage is not counted)
        """

        nums.sort()  # Step 1: Sort the input array
        result = []  # Stores unique triplets
        n = len(nums)

        for i in range(n - 2):  # We need at least 3 elements
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates
                continue

            left, right = i + 1, n - 1  # Two-pointer initialization
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Move both pointers and avoid duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1

                elif total < 0:  # Increase sum
                    left += 1
                else:  # Decrease sum
                    right -= 1
        
        return result


# Example usage
nums = [-1, 0, 1, 2, -1, -4]
sol = Solution()
print(sol.threeSum(nums))  
# Output: [[-1, -1, 2], [-1, 0, 1]]
