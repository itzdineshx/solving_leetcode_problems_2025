from collections import Counter

class Solution(object):
    def minAnagramLength(self, s):
        """
        Finds the minimum length of a substring that can be used to form an anagram of the entire string.

        :type s: str
        :rtype: int
        """
        n = len(s)

        # Check all possible substring lengths that evenly divide the total length
        for length in range(1, n + 1):
            if n % length == 0:  # The substring length must evenly divide the string length
                segment = s[:length]  # Take the first segment
                segment_freq = Counter(segment)  # Get frequency count of the first segment
                
                # Check if all segments have the same frequency distribution
                valid = True
                for i in range(0, n, length):
                    if Counter(s[i:i+length]) != segment_freq:
                        valid = False
                        break
                
                if valid:
                    return length  # Return the first valid minimum length
        
        return n  # If no smaller length found, return the full length of s

"""
### Workflow:
1. Iterate through all possible substring lengths that evenly divide `len(s)`.
2. Check if the string can be divided into equal segments.
3. Verify if each segment has the same frequency distribution.
4. Return the smallest valid length.

### Complexity:
- **Time Complexity:** O(n^2) (since checking all possible substring lengths and counting frequencies can take O(n) each)
- **Space Complexity:** O(n) (for storing frequency counts)
"""
