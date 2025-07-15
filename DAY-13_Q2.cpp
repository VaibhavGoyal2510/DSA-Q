// User function Template for C++

class Solution {
  public:
    int beautySum(string s) {
        // Your code goes here
        int count = 0;
        int n = s.size();
        
        for (int i = 0; i < n; ++i) {
            int freq[26] = {0};
            for (int j = i; j < n; ++j) {
                freq[s[j] - 'a']++;
                
                int maxF = 0, minF = INT_MAX;
                for (int k = 0; k < 26; ++k) {
                    if (freq[k] > 0) {
                        maxF = max(maxF, freq[k]);
                        minF = min(minF, freq[k]);
                    }
                }
                count += maxF - minF;
            }
        }
        return count;
    }
};