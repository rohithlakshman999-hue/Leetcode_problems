class Solution {
public:
    int shipWithinDays(vector<int>& arr, int d) {
        int n=arr.size();
        int l=0;
        int h=0;
        for(int x : arr){
            l=max(l,x);
            h+=x;
        }
        while(l<=h){
            int mid=(l+h)/2;
            int sum=0;
            int count=1;
            for(int x : arr){
                if(sum+x<=mid){
                    sum+=x;
                }
                else{
                    count++;
                    sum=x;
                }
            }
            if(count<=d){
                h=mid-1;
            }
            else{
                l=mid+1;
            }
        }
        return l;
    }
};