class Solution {
public:
    int findDuplicate(vector<int>& arr) {
        int n=arr.size();
        int l=1;
        int h=n-1;
        while(l<=h){
            int mid=(l+h)/2;
            int count=0;
            for (int i=0;i<n;i++){
                if (arr[i]<=mid){
                    count++;
                }
            }
            if (count>mid){
                 h=mid-1;
            }
            else{
                l=mid+1;
            }
        }
        return l;
    }
};