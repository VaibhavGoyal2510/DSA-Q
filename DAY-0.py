# Second Largest 


class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        first_lar =0
        sec_lar =0 
        
        for num in arr:
            if first_lar <num:
                sec_lar = first_lar
                first_lar = num
                
            elif (num >= sec_lar and num < first_lar):
                sec_lar=num
        
        # print(sec_lar)
        return sec_lar if sec_lar!=0 else -1
    