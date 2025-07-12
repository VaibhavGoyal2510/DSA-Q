#User function Template for python3

class Solution:
    def maxOdd(self, s):
        ans=""
        for i in range(len(s)-1,-1,-1):
            if int(s[i])%2!=0:
                ans+=s[i]
            
            elif len(ans)>0:
                ans+=s[i]
                
        # print(ans)
        return ans[::-1]
        # for i in range(len(ans)-1,-1,-1):
        #     if ans[i]=='0'
                
            
                
            