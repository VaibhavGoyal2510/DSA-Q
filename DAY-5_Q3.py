# Form the Largest Number

#User function Template for python3
from functools import cmp_to_key
class Solution:

	def findLargest(self,arr):
	    # code here
	   # for i in range(len(arr)):
	   #     for j in range(i+1,len(arr)):
	   #         str1= arr[i]+arr[j]
	   #         str2= arr[j]+arr[i]
	            
	   #         if int(str1)>int(str2):
	   #             pass
	            
	   #         else:
	   #             arr[i],arr[j]=arr[j],arr[i]
	                
	   
	   # for i in arr:
	   #    print(i)
	   
	   
	   
            arr = list(map(str,arr))
            
            def compare(x,y):
                if x+y>y+x:
                    return -1
                
                elif x+y<y+x:
                    return 1
                    
                else:
                    return 0
                    
            arr.sort(key=cmp_to_key(compare))
            if arr[0] == '0':
                    return '0'
            return ''.join(arr)
