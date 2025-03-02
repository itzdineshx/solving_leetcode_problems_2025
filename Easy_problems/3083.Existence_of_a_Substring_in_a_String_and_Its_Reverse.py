class Solution(object):
    def isSubstringPresent(self, s):
        """
        :type s: str
        :rtype: bool
        """

        """
        Approach:
        - Reverse the given string `s` and store it in `reverse_s`.
        - Iterate through the string `s` and extract all possible 2-character substrings.
        - Check if each extracted substring exists in `reverse_s`.
        - If a match is found, return `True`; otherwise, return `False` after the loop.
        """

        reverse_s = s[::-1]  # Reverse the string

        # Check for any two-character substring present in reverse_s
        for i in range(len(s) - 1):
            substring = s[i:i + 2]
            if substring in reverse_s:
                return True

        return False


# Example usage
sol = Solution()
s = "abca"
print(sol.isSubstringPresent(s))  # Output: True

"""
Workflow:
1. Reverse the given string.
2. Iterate through the string to extract 2-character substrings.
3. Check if the substring exists in the reversed string.
4. Return `True` if found, otherwise `False`.

Time Complexity: O(n^2) in the worst case (substring lookup in `reverse_s` is O(n)).
Space Complexity: O(n) due to storing `reverse_s`.
"""
