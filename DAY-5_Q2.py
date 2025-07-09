# Check if two Strings are Anagrams of each other


class Solution:
    def areAnagrams(self, s1, s2):
       # code here
        seen={}
       
        for s in s1:
            if s not in seen:
               seen[s]=1
              
            else:
                seen[s]+=1
               
        for s in s2:
            # print(seen[s])
            if s not in seen:
                return False 
                
            else:
                if seen[s] == 0:
                    return False
                seen[s]-=1
        
        return True
