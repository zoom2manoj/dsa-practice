import sys

from collections import defaultdict

MAX_CHARS = 256


class Solution:
    def minWindow(self, strr: str) -> str:

        n = len(strr)

        # if string is empty or having one char
        if n <= 1:
            return strr

        # Count all distinct characters.
        dist_count = len(set([x for x in strr]))

        curr_count = defaultdict(lambda: 0)
        count = 0
        start = 0
        min_len = n

        # Now follow the algorithm discussed in below
        # post. We basically maintain a window of characters
        # that contains all characters of given string.
        for j in range(n):
            curr_count[strr[j]] += 1

            # If any distinct character matched,
            # then increment count
            if curr_count[strr[j]] == 1:
                count += 1

            # Try to minimize the window i.e., check if
            # any character is occurring more no. of times
            # than its occurrence in pattern, if yes
            # then remove it from starting and also remove
            # the useless characters.
            if count == dist_count:
                while curr_count[strr[start]] > 1:
                    if curr_count[strr[start]] > 1:
                        curr_count[strr[start]] -= 1

                    start += 1

                # Update window size
                len_window = j - start + 1

                if min_len > len_window:
                    min_len = len_window
                    start_index = start

        # Return substring starting from start_index
        # and length min_len """
        return str(strr[start_index: start_index +
                                     min_len])


s = "ADOBECODEBANC"
t = "ABC"  # output BANC

solution = Solution()
data = solution.minWindow(s)

print(s, data)

