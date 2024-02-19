class Solution:
    def romanToInt(self, s: str) -> int:
        # print(s)

        data_set = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        seqeuance = {'I': 1, 'V': 2, 'X': 3, 'L': 4, 'C': 5, 'D': 6, 'M': 7}
        counter = 0
        seqeuance_track = seqeuance[s[0]]
        for index in range(len(s)):
            x = s[index]
            if seqeuance_track < seqeuance[x]:
                last_x = s[index - 1]
                counter = counter - data_set[last_x]
                counter = counter + data_set[x] - data_set[last_x]


            else:
                seqeuance_track = seqeuance[x]
                # print(x, data_set[x], seqeuance_track)
                counter = counter + data_set[x]

        print(counter)

        return counter


a = 'LVIII'
a = 'MCMXCIV'
solution = Solution()
solution.romanToInt(a)