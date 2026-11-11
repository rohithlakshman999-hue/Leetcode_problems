class Solution {
public:
    int maximumGap(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int n=nums.size();
        int x=0;
        int maxi=0;
        for (int i=1;i<n;i++){
            x=nums[i]-nums[i-1];
            maxi=max(maxi,x);
        }
        return maxi;
    }
};