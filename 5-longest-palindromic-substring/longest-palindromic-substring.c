char b[10000000];

int longest (int i,int j,char* s)
{
    while(i<=j)
    {
        if(s[i]!=s[j])
        {
            return 0;
        }
        i++;
        j--;
    }
    return 1;
}

char* longestPalindrome(char* s) {
    int i,j,k=0;
    int max=0,max_i=0,max_j=0;
    for (int i=0;i<strlen(s);i++)
    {
        for (int j=0;j<strlen(s);j++)
        {
            if(longest(i,j,s)){
            if(max<j-i+1)
            {
                max=j-i+1;
                max_i=i;
                max_j=j;
            }
        }
    }
    }
    for (int i=max_i;i<=max_j;i++)
    {
        b[k++]=s[i];
    }
    b[k]='\0';

    return b;
}