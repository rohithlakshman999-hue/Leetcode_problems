int* rearrangeArray(int* arr, int n, int* r) {
    int p=0;
    int ne=1;
    int *res = malloc(n * sizeof(int));
    for (int i=0;i<n;i++){
        if(arr[i]<0){
            res[ne]=arr[i];
            ne+=2;
        }
        else{
            res[p]=arr[i];
            p+=2;
        }
    }
    *r=n;
    return res;

}