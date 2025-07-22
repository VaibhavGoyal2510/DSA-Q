class Solution:
    def myAtoi(self, s):
        # Code here
        # ans=int(s)
        # print(ans)
        INT_MAX = 2**31 - 1   # 2147483647
        INT_MIN = -2**31 
        result=0
        sign=1
        f=0
        for ch in s:
            if ch==" ":
                continue
            
            elif ch == "-" and f==0:
                sign = -1
                
            elif ch.isdigit():
                f=1
                result=(result*10)+(ord(ch)-ord('0'))
                # print(ch,result)
                # print("Ord is ",(ord(ch)-ord('0')))
                
            else:
                break
        result=sign*result
        if result>INT_MAX:
            return INT_MAX
                    
        elif result<INT_MIN:
            return INT_MIN
            
        else:
            return result
                
                
                
                