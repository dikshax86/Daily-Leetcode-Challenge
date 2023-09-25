class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c=0
        for i in s:
            c^=ord(i)
        for j in t:
            c^=ord(j)
        return chr(c)



# class Solution:
#     def findTheDifference(self, s: str, t: str) -> str:
#         char_count={}
        
#         for i in s:
#             if i in char_count:
#                 char_count[i]+=1
#             else:
#                 char_count[i]=1
                
#         for i in t:
#             if i in char_count and char_count[i]!=0:
#                 char_count[i]-=1
#             else:
#                 return i
            
            