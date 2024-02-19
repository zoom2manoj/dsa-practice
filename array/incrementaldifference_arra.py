from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        q = []

        for index, value  in enumerate(temperatures):
            while q and value>temperatures[q[-1]]:
                res[q[-1]] = index - q[-1]
                q.pop()
            q.append(index)

        return res



temperature = [73,74,75,71,69,72,76,73]

solution = Solution()
resp = solution.dailyTemperatures(temperature)
print(resp)