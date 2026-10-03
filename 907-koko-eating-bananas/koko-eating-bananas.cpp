class Solution {
public:
    int minEatingSpeed(vector<int>& arr, int hi) {
        int n=arr.size();
        long long l = 1;
        long long h = *max_element(arr.begin(), arr.end());
        while(l<=h){
            int mid=(l+h)/2;
            long long  hour=0;
            for(int i=0;i<n;i++){
                hour+=((long long)arr[i]+mid-1)/mid;
            }
            if(hour<=hi){
                h=mid-1;
            }
            else{
                l=mid+1;
            }
        }
        return l;
    }
};