'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    def intersectPoint(self, head1, head2):
        # code here
        # Hashing
        # temp=head1
        # has={}
        
        # while temp:
        #     has[temp]=1
        #     temp=temp.next
            
        # # print(has)
        # temp=head2
        
        # while temp:
        #     if temp in has:
        #         return temp
                
        #     temp=temp.next
        # return None
        
        

        
        # Optimal
        temp1 = head1
        
        temp2=head2
        
        while(temp1!=temp2):
            temp1=temp1.next
            temp2=temp2.next
            
            if temp1==temp2:
                return temp1
                
            if temp1==None:
                temp1=head2
                
            if temp2==None:
                temp2=head1
                
                
        return temp1