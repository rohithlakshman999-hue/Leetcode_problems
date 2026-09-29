class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        vector<int> freq(1000000, 0);
        for(int i = 0; i < nums.size(); i++) {
            freq[nums[i]]++;
        }
        for(int i = 0; i < freq.size(); i++) {
            if(freq[i] == 1) {
                return i;
            }
        }
        return 0;
    }
};