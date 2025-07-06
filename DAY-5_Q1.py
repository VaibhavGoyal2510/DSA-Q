# Program to check if strings are rotations of each other 

#User function Template for python3

class Solution:
    
    #Function to check if two strings are rotations of each other or not.
    def areRotations(self,s1,s2):
        #code here
        # n=len(s1)
        
        # for i in range(len(s1)):
        #     temp=s1[0]
        #     s1=s1[1:n]
        #     s1+=temp
        #     # print(s1)
        #     if s1==s2:
        #         return True
        # # print(s1[1:n1]+s1[0])
        # return False
        
        # Both takes O(N^2) Time
         
        # text=s1+s1
        
        # while len(text)>0:
        #     print
        #     if text.startswith(s2):
        #         return True
            
        #     else:
        #         text=text[1:]
                
        # return False
        
        
        return s2 in s1+s1