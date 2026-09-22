class Solution {
public:
    vector<string> letterCombinations(string digits) {
         unordered_map<char, string> letters = {
            {'2', "abc"},
            {'3', "def"},
            {'4', "ghi"},
            {'5', "jkl"},
            {'6', "mno"},
            {'7', "pqrs"},
            {'8', "tuv"},
            {'9', "wxyz"}
        };
        vector<string> res={""};
        for(char digit : digits){
            vector<string> newr;
            for(string old : res){
                for (char ch : letters[digit]){
                    newr.push_back(old+ch);
                }
            }
            res=newr;
        }
        return res;
    }
};