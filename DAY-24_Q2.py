
class Solution:
    def reverse(self,St): 
        #code here
      
        n=len(St)
        def rec(s):
            if len(s)==1:
                num=s.pop()
                print(num,end=" ")
                # temp.append(num)
                return
            num=s.pop()
            print(num,end=" ")
            # temp.append(num)
            rec(s)
            return 
            
        rec(St)
        # return temp