int longestPalindrome(char* s) {
     int freq[128] = {0};
        int ans = 0;

        for(int i=0;i<strlen(s);i++) {
            freq[s[i]]++;
        }

        for(int i = 0; i < 128; i++) {
            ans += (freq[i] / 2) * 2;
        }

        if(ans < strlen(s)) {
            ans++;
        }

        return ans;
}