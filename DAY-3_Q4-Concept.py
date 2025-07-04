# Sliding Window 

# 4 type of questions 

# 1st Constant window 
# 2nd Longest Subarray/Substring nikalni hoti hai 
# 3rd Number of subarray based on some condition nikalni hoti hai 
# 4th Shortest / min Window based on condition nikalni hoti hai


# 1st 

# def const_window(arr,k):
#     l=0
#     r=k-1
#     summ=0
#     maxsum=0
#     for i in range(0,k):
#         summ+=arr[i]
    
#     while r<len(arr)-1:
#         summ-=arr[l]
#         l+=1
#         r+=1
#         summ+=arr[r]
        
#         maxsum =max(summ,maxsum)
        
#     return maxsum

# print(const_window([3,2,4,5,5,5,5,32,21,1],3))


# 2nd Pattern

def second_pattern(arr,k):
    l=0
    r=0
    summ=0
    max_len=0
    
    while r<len(arr):
        summ+=arr[r]
        
        while summ>k:
            summ-=arr[l]
            l+=1
            
        if summ<=k:
            max_len=max(max_len,r-l+1)
        
        print(max_len)
        r+=1
        
    return [max_len,len(arr)]

print(second_pattern([2,3,1,3,4,2,333,33,12,33,4,1,3,1,2,2,2,2,1,2,2],21))
            