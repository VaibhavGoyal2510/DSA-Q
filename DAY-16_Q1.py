class Solution:
    def setMatrixZeroes(self, mat):
        # code here
        # print(mat)
        final=[]
        for i,l in enumerate(mat):
            # print(l)
            for j,num in enumerate(l):
                # print(num)
                if num==0:
                    temp = [i,j]
                    final.append(temp)
        
        
        # 2 - Now keep i fix from that temp 
        # print(final)
        for li in final:
            i = li[0]
            
            for j in range(0,m):
                mat[i][j]=0
                
            j = li[1]
            
            for i in range(0,n):
                mat[i][j]=0
                
        return mat
        