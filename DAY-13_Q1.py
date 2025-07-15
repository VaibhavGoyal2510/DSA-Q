#User function Template for python3

class Solution:
    def countSubstring(self, s):
        # Code here
        # Brute Force but TLE
        # count=0
        # for i in range(len(s)):
            
        #     h={0:-1,1:-1,2:-1}
        #     for j in range(i,len(s)):
        #         h[ord(s[j]) - ord('a')]=1
                
        #         if (h[0]+h[1]+h[2])==3:
        #             count+=1
        # return count
        
        
        
        # # Little Better but still TLE
        # count=0
        # for i in range(len(s)):
            
        #     h={0:-1,1:-1,2:-1}
        #     for j in range(i,len(s)):
        #         h[ord(s[j]) - ord('a')]=1
                
        #         if (h[0]+h[1]+h[2])==3:
        #             count+=len(s)-j
        #             break
        # return count
                
        
        
        # Optimal
        last_seen={
            0:-1,
            1:-1,
            2:-1
        }
        count=0
        
        for i,ch in enumerate(s):
            if ch not in last_seen:
                last_seen[ord(ch) - ord('a')] = i
                
            if (last_seen[0]!=-1 and last_seen[1]!=-1 and last_seen[2]!=-1):
                count +=1+ min(last_seen[0],last_seen[1],last_seen[2])
                
        return count