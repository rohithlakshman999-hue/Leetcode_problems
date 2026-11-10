class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        stack<int> ans;
        for (int x : asteroids){
            while(!ans.empty() && ans.top()>0 && x<0){
                if (ans.top()<abs(x)){
                    ans.pop();
                }
                else if(ans.top()==abs(x)){
                    ans.pop();
                    x=0;
                    break;
                }
                else{
                    x=0;
                    break;
                }
            }
            if (x!=0){
                ans.push(x);
            }
        }
        vector<int> res;
        while (!ans.empty()){
            res.push_back(ans.top());
            ans.pop();
        }
        reverse(res.begin(),res.end());
        return res;
    }
};