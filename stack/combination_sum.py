from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        def dfs(s, pending, path):
            if pending<0:
                return
            if pending==0:
                # print(path)
                res.append(path.copy())
                print('======== ', res)
                return

            for i in range(s, len(candidates)):
                path.append(candidates[i])
                dfs(i, pending-candidates[i], path)
                path.pop()
                print('=====', path)

        candidates.sort()
        dfs(0, target, [])
        # print(res)
        return res



candidates = [2,3,6,7]
target = 7

# candidates = [10,1,2,7,6,1,5]
# target = 8

solution = Solution()

res  = solution.combinationSum(candidates, target)
print(res)