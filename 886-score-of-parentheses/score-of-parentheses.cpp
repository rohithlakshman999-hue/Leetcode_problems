class Solution {
public:
    int scoreOfParentheses(string s) {
        int score=0;
        int c=0;
        int n=s.size();
        for(int i=0;i<n;i++){
            if (s[i]=='('){
                c++;
            }
            else{
                c--;
                if(s[i-1]=='('){
                    score+=pow(2, c);
                }
            }
        }
        return score;

    }
};