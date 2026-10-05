class Solution {
public:
    int minDays(vector<int>& arr, int m, int k) {
        int n=arr.size();
        int l=0;
        int h=*max_element(arr.begin(),arr.end());
        if((long long)m*k>n){
            return -1;
        }
        while(l<=h){
            int mid=(l+h)/2;
            int s=0;
            int b=0;
            for(int i=0;i<n;i++){
                if(arr[i]<=mid){
                    s++;
                }
                else{
                    s=0;
                }
                if(s==k){
                    b++; 
                    s=0;
                }
            }
            if(b>=m){
                h=mid-1;
            }
            else{
                l=mid+1;
            }
        }
        return l;
    }
};