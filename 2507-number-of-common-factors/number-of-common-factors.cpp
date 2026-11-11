class Solution {
public:
    int commonFactors(int a, int b) {
        int mini=min(abs(a),abs(b));
        int count=0;
        for (int i=1;i<=mini;i++){
            if(a%i==0 && b%i==0){
                count++;
            }
        }
        return count;
    }
};