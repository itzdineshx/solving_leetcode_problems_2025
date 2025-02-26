class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        """
        Approach:
        - We iterate through the list of points, considering each consecutive pair.
        - The minimum time to move from one point `(x1, y1)` to `(x2, y2)` is determined by:
            - The larger of `|x2 - x1|` (horizontal distance) and `|y2 - y1|` (vertical distance).
        - This is because we can move diagonally (reducing both x and y at the same time), so the total steps required is determined by the **greater** of the two distances.
        - Accumulate this time for all point transitions.

        Why `max(abs(x2 - x1), abs(y2 - y1))`?
        - If we move diagonally, we can decrease both coordinates at once.
        - The total steps required is limited by the **longer** axis since we can handle the shorter axis simultaneously.

        """

        res = 0  # Initialize total time

        # Loop through each consecutive pair of points
        for (x1, y1), (x2, y2) in zip(points, points[1:]):
            res += max(abs(x2 - x1), abs(y2 - y1))  # Take the larger movement step

        return res  # Return the total time


# Example usage
points = [[1, 1], [3, 4], [-1, 0]]
sol = Solution()
print(sol.minTimeToVisitAllPoints(points))  # Output: 7

"""
Workflow:

1. Start at (1,1), move to (3,4):
   - |3 - 1| = 2 (horizontal distance)
   - |4 - 1| = 3 (vertical distance)
   - Steps taken = max(2, 3) = 3

2. Move from (3,4) to (-1,0):
   - |-1 - 3| = 4 (horizontal distance)
   - |0 - 4| = 4 (vertical distance)
   - Steps taken = max(4, 4) = 4

Total time: 3 + 4 = 7

Time Complexity: **O(n)**
- We iterate through the `points` list once.

Space Complexity: **O(1)**
- We use only a single variable (`res`) for storage.
"""
