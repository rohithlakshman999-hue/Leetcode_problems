class Solution(object):
    def maxValue(self, arr):
        n = len(arr)
        pre = [0]*(n+1)
        for i in range(n):
            if i%2==0:
                pre[i+1]=pre[i]+arr[i]
            else:
                pre[i+1]=pre[i]-arr[i]
        ans = pre[n]
        best = [-10**18,-10**18]
        for j in range(1,n+1):
            i=j-1
            best[i%2]=max(best[i%2],pre[i])
            ans=max(ans,pre[n]+2*(best[j % 2]-pre[j]))
        return ans