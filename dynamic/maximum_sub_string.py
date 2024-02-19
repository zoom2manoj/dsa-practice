class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
	    # n is the possible most repeating unit
        n = len(sequence) // len(word)

        while n:
            print(word*n)
            if word * n in sequence:
                return n
            n -= 1
        return 0

solution = Solution()
seq = 'aaabaaaabaaabaaaabaaaabaaaabaaaaba'
word = 'aaaba'
value = solution.maxRepeating(seq, word)

print(value)