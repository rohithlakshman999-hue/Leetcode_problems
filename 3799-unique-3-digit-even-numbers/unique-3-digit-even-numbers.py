class Solution(object):
    def totalNumbers(self, arr):
        n=len(arr)
        count=0
        ans=set()
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i!=k and i!=j and j!=k:
                        if arr[i]!=0 and arr[k]%2==0:
                            num=arr[i]*100+arr[j]*10+arr[k]
                            ans.add(num)

        return len(ans)