import sys


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        target_map = {}
        for x in t:
            if x in target_map:
                target_map[x] = target_map[x]+1
            else:
                target_map[x] = 1
        print(target_map)

        count = 0
        begin = 0
        end = 0
        min = sys.maxsize
        head = 0

        while end<len(s):
            c = s[end]
            if c in target_map:
                target_map[c]-=1
                if target_map[c]>=0:
                    count+=1
            end+=1
            print(count, end)
            while count == len(t):
                if end-begin < min:
                    head = begin
                    min = end-head
                    print('min', min)
                tempc = s[begin]
                if tempc in target_map:
                    target_map[tempc] = target_map[tempc]+1
                    if target_map[tempc]>0:
                        count-=1
                begin+=1
            
            print(head, min, head+min, s[head:head+min])









s = "ADOBECODEBANC"
t = "ABC"  # output BANC

solution = Solution()
data = solution.minWindow(s, t)

