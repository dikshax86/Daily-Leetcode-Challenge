from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        def binary_search(arr):
            l=0
            r=len(arr)-1
            arr=[0]+arr+[0]
            ans=0
            
            while l<=r:
                
                mid=(l+r)//2
                
                if arr[mid]>=arr[mid-1] and arr[mid]>=arr[mid+1]:
                     return mid
                
                elif arr[mid]<arr[mid-1]:
                    r=mid-1
                    
                else:
                    l=mid+1
                    
            return ans
                    
        return binary_search(arr)-1