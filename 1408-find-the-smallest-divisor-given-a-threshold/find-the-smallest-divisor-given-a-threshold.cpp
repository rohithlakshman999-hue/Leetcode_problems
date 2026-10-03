class Solution {
public:
    int smallestDivisor(vector<int>& arr, int t) {
        int n=arr.size();
        int l=1;
        int h = *max_element(arr.begin(), arr.end());
        while(l<=h){
            int mid=(l+h)/2;
            int s=0;
            for(int i=0;i<n;i++){
                s+=(arr[i]+mid-1)/mid;
            }
            if(s<=t){
                h=mid-1;
            }
            else{
                l=mid+1;
            }
        }
        return l;
    }
};