class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        """
        Approach:
        - We process the matrix in a **spiral order** by removing elements layer by layer.
        - We follow four steps in a loop:
            1. Extract the **top row** (left to right).
            2. Extract the **rightmost column** (top to bottom).
            3. Extract the **bottom row** (right to left, if it exists).
            4. Extract the **leftmost column** (bottom to top, if it exists).
        - We continue until the matrix is empty.

        Edge Cases:
        - If the matrix is empty, return an empty list.
        - If the matrix has only one row or one column, it should be handled correctly.
        """

        ret_mat = []  # Result list to store elements in spiral order

        while matrix:
            # Step 1: Take the first row (left to right)
            ret_mat += matrix.pop(0)

            # Step 2: Take the last column (top to bottom)
            if matrix and matrix[0]:  # Ensure matrix is not empty after pop
                for row in matrix:
                    ret_mat.append(row.pop())

            # Step 3: Take the last row (right to left)
            if matrix:
                ret_mat += matrix.pop()[::-1]  # Reverse the last row before adding

            # Step 4: Take the first column (bottom to top)
            if matrix and matrix[0]:
                for row in matrix[::-1]:  # Iterate in reverse order
                    ret_mat.append(row.pop(0))

        return ret_mat


# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

sol = Solution()
print(sol.spiralOrder(matrix))  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]


"""
Workflow:

Given Matrix:
[
    [1,  2,  3],
    [4,  5,  6],
    [7,  8,  9]
]

Steps:
1. Extract top row → `[1, 2, 3]`
2. Extract rightmost column → `[6, 9]`
3. Extract bottom row (reversed) → `[8, 7]`
4. Extract leftmost column (bottom to top) → `[4]`
5. Extract remaining top row → `[5]`

Final Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
 
Time Complexity: **O(m × n)**
- Every element is visited **exactly once**, so the complexity is **O(m × n)**.

Space Complexity: **O(1)**
- The output list `ret_mat` is the only additional space used (excluding input matrix modifications).
"""
