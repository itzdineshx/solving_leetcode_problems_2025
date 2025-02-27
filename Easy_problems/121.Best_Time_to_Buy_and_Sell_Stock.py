class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        """
        Approach:
        - We traverse the array while keeping track of the **minimum price seen so far**.
        - On each day, we calculate the **potential profit** if we were to sell at the current day's price.
        - We update the **maximum profit** whenever we find a new higher profit.
        - If the stock price is lower than the minimum price, we update the minimum price.

        Edge Cases:
        - If there is only one price, no profit can be made.
        - If prices are strictly decreasing, return 0 (no profitable transactions).
        """

        # Initialize minimum price as a very high number
        min_price = float('inf')
        max_profit = 0  # Initialize max profit

        for price in prices:
            # Update the minimum price if the current price is lower
            if price < min_price:
                min_price = price

            # Calculate profit if selling on this day and update max_profit if it's higher
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit


# Example usage
prices = [7, 1, 5, 3, 6, 4]
sol = Solution()
print(sol.maxProfit(prices))  # Output: 5


"""
Workflow:

Given prices: [7, 1, 5, 3, 6, 4]

Step-by-step tracking:
1. min_price = 7, max_profit = 0
2. min_price = 1 (new minimum found)
3. max_profit = 4 (5 - 1)
4. max_profit remains 4 (3 - 1 < 4)
5. max_profit = 5 (6 - 1)
6. max_profit remains 5 (4 - 1 < 5)

Final result: max_profit = 5

Time Complexity: O(n)
- We traverse the prices list **only once**.

Space Complexity: O(1)
- We only use two variables (`min_price` and `max_profit`).
"""
