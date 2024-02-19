from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        candidates.sort()

        def dfs(s, pending, path):

            if pending<0:
                return
            if pending==0:
                res.append(path.copy())
                return

            for i in range(s, len(candidates)):
                if i>s and candidates[i]==candidates[i-1]:
                    continue
                path.append(candidates[i])
                dfs(i+1, pending-candidates[i], path)
                path.pop()


        dfs(0, target, [])
        print(res)


        return res



candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
solution = Solution()
solution.combinationSum2(candidates, target)
