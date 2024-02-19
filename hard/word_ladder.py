import collections
from typing import List
import string


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]):

        wordset  = set(wordList)

        if endWord not in wordset:
            return 0
        counter = 1
        q = []
        visited = set()
        q.append(beginWord)
        while len(q) > 0:
            print("=================")
            for index in range(len(q)):
                word = q.pop()
                visited.add(word)
                # print(word)
                if word == endWord:
                    return counter
                for i in range(len(word)):
                    # print('===')
                    for j in range(ord('a'), ord('z')):
                        wc = list(word)
                        wc[i] = chr(j)
                        twc = ''.join(wc)
                        # print('twc', twc)
                        if twc not in visited:
                            q.append(twc)
                            visited.add(twc)
                # print(q, visited)
            print(counter)

            counter += 1
        return 0

    def ladderLength2(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        ans = 0
        q = collections.deque([beginWord])

        while q:
            ans += 1
            for _ in range(len(q)):
                wordList = list(q.popleft())
                # print(wordList, 'man')
                print(enumerate(wordList))
                print(wordList)
                for i, cache in enumerate(wordList):
                    for c in string.ascii_lowercase:
                        wordList[i] = c
                        word = ''.join(wordList)
                        if word == endWord:
                            return ans + 1
                        if word in wordSet:
                            q.append(word)
                            wordSet.remove(word)
                    print(wordList, cache)
                    wordList[i] = cache
                    print(wordList)
                    print('====')

        return 0

solution = Solution()
a = "ymain"
b = "oecij"
c = ["ymann", "yycrj", "oecij", "ymcnj", "yzcrj", "yycij", "xecij", "yecij", "ymanj", "yzcnj", "ymain"]
output = solution.ladderLength2(a, b, c)
print(output)
