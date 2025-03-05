class Solution(object):
    def coloredCells(self, n):
        """
        Given an integer n, returns the total number of colored cells in a pattern that expands 
        in a spiral-like manner. The pattern follows the formula:
        
            Total Colored Cells = n^2 + (n+1)^2
        
        This formula is derived from observing the pattern:
            - For n = 0, colored cells = 0^2 + 1^2 = 0 + 1 = 1
            - For n = 1, colored cells = 1^2 + 2^2 = 1 + 4 = 5
            - For n = 2, colored cells = 2^2 + 3^2 = 4 + 9 = 13
            - For n = 3, colored cells = 3^2 + 4^2 = 9 + 16 = 25
            - and so on.
        
        Alternatively, the formula can also be written as: 2*n*(n+1) + 1
        
        :type n: int
        :rtype: int
        """
        # Using the formula: n^2 + (n+1)^2
        return (n-1)**2+n**2


"""
Workflow:
1. Observe the pattern of colored cells based on the input n:
   - For n = 0: 0^2 + 1^2 = 1
   - For n = 1: 1^2 + 2^2 = 1 + 4 = 5
   - For n = 2: 2^2 + 3^2 = 4 + 9 = 13
   - For n = 3: 3^2 + 4^2 = 9 + 16 = 25
2. Recognize that the formula n^2 + (n+1)^2 (or equivalently 2*n*(n+1) + 1) correctly generates the number of colored cells.
3. Return the computed value using this formula.

Time Complexity: O(1)
    - The computation involves only a few arithmetic operations.
Space Complexity: O(1)
    - No additional data structures are used apart from a few variables.
    
Example:
    For n = 2, the function returns 2^2 + 3^2 = 4 + 9 = 13.
"""
