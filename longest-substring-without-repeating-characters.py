class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [-1] * 256
        left = right = 0
        n = len(s)
        length = 0
        result = 0
        while right < n:
            x = s[right]
            if chars[ord(x)] > -1:
                if chars[ord(x)] + 1 > left:
                    left = chars[ord(x)] + 1
                chars[ord(x)] = right
            else:
                chars[ord(x)] = right
            right += 1

            result = max(result, right - left)
            print(x, left, right, right - left)

        return result

solution = Solution()
value = solution.lengthOfLongestSubstring(s)
print(value)


data = 'pwwkew'