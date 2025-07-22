class Solution:
    def longestPalindrome( s):
        # Works good for finding out max_length but can't find the substring
        
        # # code here
        # max_l=0
        # index_start=-1
        # index_end=-1
        # for i in range(len(s)):
        #     temp=0
        #     t=i
        #     j=len(s)-1
        #     t_st=-1 #temperory start index 
        #     t_end=-1 #temprorry ending index
        #     # print("Phase -",i)
        #     f=0
        #     while t<=j:
        #         # print(f"t is {t} and j is {j}")
        #         if s[t]==s[j] and t!=j:
        #             # print("hello ",s[t])
        #             if temp==0:
        #                 t_st=t
        #                 t_end=j
        #             temp+=2
        #             t+=1
        #             j-=1
        #             # print("And temp is ",temp)
                    
        #         elif s[t]==s[j] and t==j:
        #             # print("hello 2 ",s[t])
        #             if temp==0:
        #                 t_st=t
        #                 t_end=j
        #             temp+=1
        #             t+=1
        #             j-=1
        #             f=1
        #             # print("And temp is ",temp)
                    
                    
        #         elif s[t]!=s[j] and temp>0:
        #             t=i
        #             # j-=1
        #             # if max_l<temp:
        #             #     index_start=t_st
        #             #     index_end=t_end
        #             max_l=max(max_l,temp)
        #             t_st=-1
        #             t_end=-1
        #             temp=0
                    
        #         elif s[t]!=s[j]:
        #             j-=1
                    
        #     # Final updations
        #     # # t_end=j+1
        #     # if max_l<temp:
        #     #             index_start=t_st
        #     #             index_end=t_end
        #     max_l=max(max_l,temp)
        # print(f"After phase/ max is {max_l} and start {index_start} & end is {index_end}")
        
        # ans = s[index_start:index_end+1]
        # return ans
        
        
        # For finding substring
        # Solution from YT
        ans=""
        ans_len=0
        
        for i in range(len(s)):
            #Odd length 
            l,r=i,i
            
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>ans_len:
                    ans=s[l:r+1]
                    ans_len=r-l+1
                    
                l-=1
                r+=1
                
            # Even Length
            l,r=i,i+1
            
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>ans_len:
                    ans=s[l:r+1]
                    ans_len=r-l+1
                    
                l-=1
                r+=1
                
        return ans
            
babe =Solution

print(babe.longestPalindrome("gklababamkji"))