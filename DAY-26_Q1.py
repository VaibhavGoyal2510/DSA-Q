from typing import Optional


from typing import List

"""

Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None

You can also use the following for printing the link list.
displayList(node)
"""

class Solution:
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        # code here
        hel={}
        
        temp = head
        ans=[]
        
        while temp:
            num = target-temp.data
            
            if num<0:
                temp=temp.next
                continue
            # print(num)
            # print("hel is ",hel)
            if num in hel:
                # print("kya hai")
                if temp.data<num:
                    b=(temp.data,num)
                    
                else:
                    b=(num,temp.data)
                ans.append(b)
                
            hel[temp.data]=1
            temp=temp.next
            
        return ans[::-1]
                
            
        
