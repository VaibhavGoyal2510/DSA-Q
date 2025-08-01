'''
	Function Arguments: head of the original list.
	Return Type: head of the new list formed.
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}'''
	
class Solution:
    def segregate(self, head):
        #code here
        if head == None or head.next==None:
            return head
            
        temp = head
        l=[]
        while temp:
           l.append(int(temp.data))
           temp=temp.next
           
        # Using dutch National Flag algo
        low = 0
        mid = 0
        high = len(l)-1
        
        while mid<=high:
            if l[mid]==0:
                l[low],l[mid]=l[mid],l[low]
                low+=1
                mid+=1
                
            elif l[mid]==1:
                mid+=1
                
            else:
                l[high],l[mid]=l[mid],l[high]
                high-=1
                
        # print(l)
        
        temp = head
        i=0
        while temp and i<len(l):
           temp.data=l[i]
           i+=1
           temp=temp.next
           
        return head
                
                
    