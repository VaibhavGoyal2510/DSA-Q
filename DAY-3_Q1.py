# Stock Buy and Sell – Max one Transaction Allowed

class Solution:
    def maximumProfit(self, prices):
        # code here
        # if len(prices)==1:
        #     return 0
            
        # mini = 0
        # maxi = 0
        # max_profit=0
        # for i in range(len(prices)):
        #     if mini>maxi:
        #         maxi=mini
        #     if prices[maxi]<= prices[i]:
        #         maxi = i
                
        #     if prices[mini]>=prices[i]:
        #         mini = i
                
        #     # print("Dekho ",prices[maxi]-prices[mini],maxi,mini)
        #     if(mini<maxi): max_profit = max(max_profit,prices[maxi]-prices[mini])
            
        # print(mini,maxi)
                
        # return max_profit 
        
        
        # Solution
        
        mini= prices[0]
        maxi=0
        for i in range(1,len(prices)):
            if prices[i]>mini:
                maxi=max(maxi,prices[i]-mini)
                
            else:
                mini=prices[i]
                
        return maxi
        
        
        
        