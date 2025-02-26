#Base solition
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        """
        Approach:
        - Use a nested loop to check every pair of numbers in `nums`.
        - Iterate through `nums` using two indices (`i` and `j`).
        - For each number at index `i`, check if there exists another number at index `j > i` such that `nums[i] + nums[j] == target`.
        - If such a pair is found, return their indices `[i, j]`.

        Why Nested Loops?
        - This is the brute-force approach.
        - It ensures we check all possible pairs exhaustively.
        - It does not require extra space but is less efficient than the hash map approach.
        """

        n = len(nums)  # Get the length of the list

        for i in range(n):
            for j in range(i + 1, n):  # Ensure j > i to avoid repeating pairs
                if nums[i] + nums[j] == target:  # Check if sum matches target
                    return [i, j]  # Return the indices

# Example usage
nums = [2, 7, 11, 15]
target = 9
sol = Solution()
print(sol.twoSum(nums, target))  # Output: [0, 1]

"""
Workflow:

1. Iterate through the list using index `i`.
2. For each `i`, iterate through the remaining elements using index `j`.
3. Check if `nums[i] + nums[j] == target`.
4. If a match is found, return `[i, j]`.

Example Walkthrough:

nums = [2, 7, 11, 15], target = 9

Iteration 1: i=0, nums[i]=2
   - j=1, nums[j]=7 → 2+7=9 ✅ → return [0,1]

Output = [0, 1]

Time Complexity: O(n²)
   - Outer loop runs `n` times.
   - Inner loop runs `n-1`, `n-2`, ..., 1 times → O(n²).

Space Complexity: O(1)
   - No extra space used apart from variables.
"""

# optimized solution
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        """
        Approach:
        - Use a hash map (dictionary) to store previously seen numbers and their indices.
        - Iterate through the list using `enumerate()` to get both index and value.
        - For each number, compute `diff = target - value`:
            - If `diff` exists in the hash map, return the indices of `diff` and `value`.
            - Otherwise, store the current number in the hash map with its index as the key.

        Why Hash Map?
        - Hash maps allow O(1) lookup time for checking if `diff` exists.
        - This avoids a nested loop, reducing time complexity from O(n²) to O(n).
        """

        hash_map = {}  # Dictionary to store number-index pairs

        for index, value in enumerate(nums):
            diff = target - value  # Calculate the difference needed
            if diff in hash_map:  
                return [index, hash_map[diff]]  # Found the pair
            hash_map[value] = index  # Store the value with its index

# Example usage
nums = [2, 7, 11, 15]
target = 9
sol = Solution()
print(sol.twoSum(nums, target))  # Output: [1, 0]

"""
Workflow:

1. Initialize an empty hash_map (dictionary).
2. Loop through nums:
   - Compute `diff = target - value`
   - If `diff` is in `hash_map`, return `[index, hash_map[diff]]`
   - Otherwise, store `value` in `hash_map` with its index.

Example Walkthrough:

nums = [2, 7, 11, 15], target = 9

Iteration 1: (index=0, value=2)
- diff = 9 - 2 = 7
- 7 is NOT in hash_map
- Store 2 at index 0 → hash_map = {2: 0}

Iteration 2: (index=1, value=7)
- diff = 9 - 7 = 2
- 2 is in hash_map → return [1, 0] ✅

Output = [1, 0]

Time Complexity: O(n)
   - Each lookup and insertion in the dictionary takes O(1).
   - We iterate through `nums` once → O(n).

Space Complexity: O(n)
   - Worst case: We store all numbers in `hash_map`.
"""
