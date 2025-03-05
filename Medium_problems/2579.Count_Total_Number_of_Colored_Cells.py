class Solution(object):
    def coloredCells(self, n):
        """
        Given an integer n, returns the total number of colored cells in a spiral-like pattern.
        
        The pattern follows the formula:
            Total Colored Cells = (n - 1)^2 + n^2
        
        This formula is derived from observing the pattern:
            - For n = 1, colored cells = (1 - 1)^2 + 1^2 = 0 + 1 = 1
            - For n = 2, colored cells = (2 - 1)^2 + 2^2 = 1 + 4 = 5
            - For n = 3, colored cells = (3 - 1)^2 + 3^2 = 4 + 9 = 13
            - For n = 4, colored cells = (4 - 1)^2 + 4^2 = 9 + 16 = 25
            - and so on.
        
        Alternatively, this formula can be expressed as:
            2*n^2 - 2*n + 1
        
        :type n: int
        :rtype: int
        """
        # Compute the total number of colored cells using the formula: (n - 1)^2 + n^2
        return (n - 1)**2 + n**2


"""
Workflow:
1. Input an integer n, representing the step number in the spiral expansion.
2. Calculate the number of colored cells using the formula:
       Total Colored Cells = (n - 1)^2 + n^2
   - For n = 1: (1-1)^2 + 1^2 = 0 + 1 = 1
   - For n = 2: (2-1)^2 + 2^2 = 1 + 4 = 5
   - For n = 3: (3-1)^2 + 3^2 = 4 + 9 = 13
   - For n = 4: (4-1)^2 + 4^2 = 9 + 16 = 25
3. Return the computed result.

Time Complexity: O(1)
    - The computation involves only a fixed number of arithmetic operations.
Space Complexity: O(1)
    - No additional data structures are used apart from basic variables.
"""
