class Solution {
public:
    string replaceDigits(string arr) {
        int n = arr.size();
        string ans="";
        ans.push_back(arr[0]);
        for(int i=1;i<n;i++){
            if(arr[i]>='a' && arr[i]<='z'){
                ans.push_back(arr[i]);
            }
            else{
                ans.push_back(arr[i-1]+(arr[i]-'0'));
            }
        }
        return ans;   
    }
};