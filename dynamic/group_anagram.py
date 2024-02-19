from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = {}

        for x in strs:
            print('value', x)
            item = ''.join(sorted(x))
            print(item)

            if item not in result:
                result[item] = [str(x)]
            else:
                result[item].append(str(x))



        return [result[x] for x in result.keys()]



input = ["eat","tea","tan","ate","nat","bat"]
solution = Solution()
res = solution.groupAnagrams(input)
print(res)
