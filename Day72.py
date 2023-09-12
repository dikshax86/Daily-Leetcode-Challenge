class Solution:
    def minDeletions(self, s: str) -> int:
        
        c_count=[0]*26
        
        for i in s:
            c_count[ord(i)-97]+=1
        
        result_arr=[]
        for i in c_count:
            if i:
                result_arr.append(i)
        
        result_arr=sorted(result_arr, reverse=True)
        
        i=0
        while i<len(result_arr)-1:
            j=i+1
            
            while j<len(result_arr):
                if result_arr[j]==result_arr[i]:
                    result_arr[j]=result_arr[j-1]-1
                if result_arr[j]<0:
                    result_arr[j]=0
                j+=1
            i+=1
        
        return sum(c_count)-sum(result_arr)
            
            