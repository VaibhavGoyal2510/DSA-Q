'''

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''
#Function to check whether the list is palindrome.
class Solution:
    def isPalindrome(self, head):
        #code here
        # Works for 0-9 elements in LL
        # if head ==None:
        #     return False
            
            
        # temp = head
        # num=0
        # while temp:
        #     num=(num*10)+int(temp.data)
            
        #     temp=temp.next
            
        # # print(num)
        # # Now check if that num is palindrome or not
        
        # ans = str(num)
        
        # i=0
        # j=len(ans)-1
        
        # while i<=j:
        #     if ans[i]==ans[j]:
        #         i+=1
        #         j-=1
                
        #     else:
        #         return False
                
        # return True
        
        
        # #Another Approach - Stack - SC -O(N) & TC-> O(2*N)
        # if head == None:
        #     return False
        
        # stack=[]
        
        # temp = head 
        # f=0
        # while temp:
        #     # print(temp.data,"flag ",f)
        #     stack.append(temp.data)
        #     temp=temp.next
            
        # # print(stack)
        # temp = head
        
        # while temp:
        #     el = stack.pop()
        #     # print(el,temp.data)
        #     if temp.data!=el:
        #         return False
        #     temp=temp.next
                
        # return True
        
        
        # TC same but O(1) space
        
        if head ==None:
            return False
            
        slowptr=head
        fastptr=head
        count=-1
        temp=None
        while fastptr!=None and fastptr.next!=None:
            count+=1
            temp=slowptr
            slowptr=slowptr.next
            fastptr=fastptr.next.next
            
        first=head
        if count%2==0:
            second=slowptr
            
        else:
            second=temp
            
        # Reverse a Linked List
        
        # print(second.next.data)
        curr = second
        nex =None
        
        while curr:
            t = curr.next
            
            curr.next=nex
            nex=curr
            second=curr
            curr=t
        
        # print(first.data)
        # Now checking both of these
        while first and second:
            
            if first.data != second.data:
                return False
                
            first=first.next
            second=second.next
            
        return True