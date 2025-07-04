# Repeated sum of digits
#User function Template for python3

# Conccept was sum of repetitive digits = this abcd % 9 i.e gives same answer
class Solution:
    def repeatedSumOfDigits (self,num):
        # code here 
        # print(type(N))
        if num == 0 :
            return 0
        
        if num % 9 ==0:
            return 9
            
            
        return num%9