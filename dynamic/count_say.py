
class Solution:
    def countAndSay(self, n: int) -> str:
        i=0
        seq = '1'

        while i<n:
            print(i)
            output = ''
            value = ''
            count = 0
            for index in range(len(seq)):
                item = seq[index]
                print(item)
                if value=='':
                    value = item
                    count+=1
                elif value==item:
                    count+=1
                else:
                    output = output+str(count)+value
                    count=1
                    value = item
            output = output+str(count)+value
            seq = output
            print(output)
            i+=1
        return seq



n = 4
solution = Solution()
ss = solution.countAndSay(n)
print('============================')
print('ss', ss)
print('expected ', '1211')