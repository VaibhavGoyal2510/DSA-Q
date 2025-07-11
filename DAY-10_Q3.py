#User function Template for python3
# Outermost Parentheses
class Solution:
    def removeOuter(self, s):
        # Code here
        stack=[]
        ans=""
        count_in=0
        for ch in s:
            if ch=='(' and len(stack)>0:
                ans+=ch
                count_in+=1
            elif ch==')' and count_in>0:
                ans+=ch
                count_in-=1

            elif ch=='(':
                stack.append(ch)
            else:
                stack.pop()

        return ans