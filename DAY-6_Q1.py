# Absolute diagonal difference in a square matrix

class Solution:
    def diagonalSumDifference(self,N,Grid):
        #code here
        sum1=0
        sum2=0
        did=len(Grid)-1
        for i in range(len(Grid)):
            
            sum1+=Grid[i][i]
            sum2+=Grid[i][did]
            did-=1
            
            # print(sum1,sum2)
            
        return abs(sum1-sum2)