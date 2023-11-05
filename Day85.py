class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        
        if k>=len(arr):return max(arr)
        
        max_val=max(arr[0],arr[1])
        winc=1
        last=max_val
        
        for i in range(2,len(arr)):
            
            if winc==k:
                return max_val
            
            if arr[i]>max_val:
                max_val=arr[i]
                last=arr[i]
                winc=1
                
            else:
                winc+=1
        
    
        return max_val
