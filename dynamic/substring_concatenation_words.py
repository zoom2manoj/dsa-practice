from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        word_total_size = word_len*len(words)
        words_map = {}
        result = []
        if word_total_size>len(s):
            return result
        for word in words:
            if word in words_map:
                words_map[word]+=1
            else:
                words_map[word] = 1
        print('word map', words_map)
        for i in range(len(s)-word_total_size+1):
            j =i
            temp_word_map = words_map.copy()
            count = len(words)
            while j<i+word_total_size:
                item = s[j:j+word_len]
                if item not in words_map or temp_word_map[item]==0:
                    break
                else:
                    temp_word_map[item]-=1
                    count-=1

                j+=word_len
                print(count)
            if count==0:
                result.append(i)

        print('result', result)
        return result




s = "barfoothefoobarman"
L = ["foo", "bar"]
solution = Solution()

solution.findSubstring(s, L)