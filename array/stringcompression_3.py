from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        last = None
        count = 0
        indexing = 0
        for i,  c in enumerate(chars):
            if last is None:
                last = c
                count +=1
            elif last!=c:
                print(count, c, last, indexing)
                chars[indexing]=last
                indexing+=1
                if count>1:
                    for value in str(count):

                        chars[indexing] = value
                        indexing += 1

                last = c
                count = 1
            elif last ==c :
                count+=1
            if i==len(chars)-1:
                print(count, c, last, indexing)
                chars[indexing] = last
                indexing += 1
                if count > 1:
                    for value in str(count):
                        chars[indexing] = value
                        indexing += 1





            # print(c)

        print(chars, indexing)
        return indexing

s = ["a","a","b","b","c","c","c"]
# s = ["a","b","c"]
s = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]



solution = Solution()
solution.compress(s)
print(s)