class Solution {
public:
    bool searchMatrix(vector<vector<int>>& mat, int t) {
        int n =mat.size();
        int m=mat[0].size();
        int i=0;
        int j=(n*m)-1;
        while(i<=j){
            int mid=i+(j-i)/2;
            if(mat[mid/m][mid%m]==t){
                return true;
            }
            if(mat[mid/m][mid%m]<t){
                i=mid+1;
            }
            else{
                j=mid-1;
            }
        }
        return false;
    }
};