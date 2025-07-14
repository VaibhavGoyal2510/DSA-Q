class Solution:
    def romanToDecimal(self, s): 
        # code here
        roman = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        ans = 0
        for i,ch in zip(range(len(s)-1,-1,-1),s[::-1]):
            # print("Value for ",ch,"is ->",roman[ch])
            if i==len(s)-1:
                ans+=roman[ch]
            
            elif roman[ch]<roman[s[i+1]]:
                ans-=roman[ch]
            else:
                ans+=roman[ch]
        
        return ans