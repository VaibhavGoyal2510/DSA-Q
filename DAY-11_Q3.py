class Solution:
    def areIsomorphic(self, s1, s2):
        # code here 
        h1={}
        h2={}
        
        for i in range(len(s1)):
            
            if s1[i] not in h1:
                h1[s1[i]] = i
            
            if s2[i] not in h2:
                h2[s2[i]]= i
                
                
            if h1[s1[i]]!=h2[s2[i]]:
                return False
                
        return True