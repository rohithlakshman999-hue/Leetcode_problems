class Solution(object):
    def search(self, arr, t):
        n=len(arr)
        l=0
        h=n-1
        while(l<=h):
            mid=(l+h)//2
            
            if arr[mid]==t:
                return True

            if arr[l]==arr[mid] and arr[h]==arr[mid]:
                l+=1
                h-=1
                continue
            if arr[l]<=arr[mid]:
                if arr[l]<=t and t<=arr[mid]:
                    h=mid-1
                else:
                    l=mid+1
            else:
                if arr[mid]<=t and t<=arr[h]:
                    l=mid+1
                else:
                    h=mid-1

        return False

            
        