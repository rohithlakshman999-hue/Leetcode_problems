class Solution {
public:
    int maxProduct(vector<int>& arr) {
        int n=arr.size();
        int curmax=arr[0];
        int curmin=arr[0];
        int ans=arr[0];

        for (int i=1;i<n;i++){
            int x=arr[i];

            int tempmax=max(x,max(x*curmax,x*curmin));
            int tempmin=min(x,min(x*curmax,x*curmin));

            curmax=tempmax;
            curmin=tempmin;

            ans=max(ans,curmax);
        }
        return ans;
    }
};