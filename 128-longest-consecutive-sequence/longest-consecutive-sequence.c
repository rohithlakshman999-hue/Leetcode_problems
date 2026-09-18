#include <stdlib.h>

int compare(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int longestConsecutive(int* arr, int n) {

    if (n == 0) {
        return 0;
    }

    qsort(arr, n, sizeof(int), compare);

    int max = 1;
    int count = 1;

    for (int i = 1; i < n; i++) {

        if (arr[i] == arr[i - 1]) {
            continue;
        }
        else if (arr[i] == arr[i - 1] + 1) {
            count++;
        }
        else {
            count = 1;
        }

        if (count > max) {
            max = count;
        }
    }

    return max;
}