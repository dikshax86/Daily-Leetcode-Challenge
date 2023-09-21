from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i,j=0,0
        li=[]
        
        nums1.append(10**7)
        nums2.append(10**7)
        
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<=nums2[j]:
                li.append(nums1[i])
                i+=1
            else:
                li.append(nums2[j])
                j+=1
            
        li.pop()
        lth=len(li)
        mid=lth//2
        
        if lth%2:
            return li[mid]
        else:
            return (li[mid]+li[mid-1])/2
        