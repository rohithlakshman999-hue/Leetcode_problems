class Solution {
public:
    int subarraySum(vector<int>& arr, int k) {
        unordered_map<int,int> freq;
        int sum = 0;
        int count = 0;
        freq[0] = 1;

        for(int x : arr) {
            sum += x;
            if(freq.find(sum - k) != freq.end()) {
                count += freq[sum - k];
            }
            freq[sum]++;
        }
        return count;
    }
};