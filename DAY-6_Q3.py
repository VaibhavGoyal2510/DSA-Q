# Double val of nth Node from end in a linked list

'''
	A linked list node has the following structure
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
#Function to find the data of kth node from the end of a linked list
class Solution:
    def getKthFromLast(self, head, k):
        #code here
        temp = head 
        count=0
        last=head
        while temp!=None:
            # print(temp.data)
            last=temp
            temp=temp.next
            count+=1
        if k>count: return -1
        # print(last.data,count)
        
        if k==1: return last.data
        
        temp=head
        final=count-k
        ans=0
        while final>=0:
            ans=temp.data
            temp=temp.next
            final-=1
            
        return ans
        
        