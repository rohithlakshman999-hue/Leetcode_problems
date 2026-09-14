bool canConstruct(char* a, char* b) {
    int n = strlen(a);
    int n1=strlen(b);
    bool found = false;
    int freq[26]={0};
    int freq1[26]={0};
    for (int i=0;i<n;i++){
        freq[a[i]-'a']++;
    }
    for (int i=0;i<n1;i++){
        freq[b[i]-'a']--;
    }

    for(int i=0;i<26;i++){
        if(freq[i]>0){
            return false;
        }
    }
    return true;
}