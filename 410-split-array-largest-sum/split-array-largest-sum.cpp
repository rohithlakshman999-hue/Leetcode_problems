class Solution {
public:
    int splitArray(vector<int>& arr, int k) {
        int n=arr.size();
        int l=*max_element(arr.begin(),arr.end());
        int h=0;
        for(int i=0;i<n;i++){
            h+=arr[i];
        }
        while(l<=h){
            int mid=(l+h)/2;
            int sum=0;
            int count=1;
            for(int i=0;i<n;i++){
                if (sum+arr[i]<=mid){
                    sum+=arr[i];
                }
                else{
                    count+=1;
                    sum=arr[i];
                }
            }
            if (count<=k){
                h=mid-1;
            }
            else{
                l=mid+1;
            }
        }
        return l;
    }
};