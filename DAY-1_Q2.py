# Three Great Candidates

def maxProduct( arr):
        # code here
        max1=max2=max3 = float('-inf')
        small=min2 = float('inf')
        
        for num in arr:
            if num>= max1:
                max3=max2
                max2=max1
                max1=num
            
            elif num>=max2 and num<max1:
                max3=max2
                max2=num
                
            elif num>=max3 and num<max2:
                max3=num
                
        for num in arr:
            if small>=num:
                min2=small
                small=num
                
            elif num>=min2 and num<small:
                min2=num
                
        # print(max1,max2,max3,max1*max3*max2)
        print(small,min2)
        if small>max1 or min2>max1: return (max1*max2)*max3
        
                
        return (max1*max2)*max3 if (max1*max2)*max3 > small*min2*max1 else small*min2*max1
    
arr= [852,-566,182,-638,-693,-323]

print(maxProduct(arr))