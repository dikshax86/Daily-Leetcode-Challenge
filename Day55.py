class TrieNode():
    def __init__(self):
        self.ref=[None]*26
        self.isEnd=False
        
class Solution:
    def __init__(self):
        self.root=TrieNode()
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def insert(word):
            temp=self.root
            for c in word:
                c=ord(c)-97
                if not temp.ref[c]:
                    temp.ref[c]=TrieNode()
                temp=temp.ref[c]
            temp.isEnd=True
        
        def searchTrie(word):
            temp=self.root
            for c in word:
                c=ord(c)-97
                if temp.ref[c]:
                    temp=temp.ref[c]
                else:
                    return False
                
            return True if temp.isEnd else False
                
            
        for word in wordDict:
            insert(word)
        
        dp=[False]*(len(s)+1)
        dp[0]=True
        
        for i in range(1,len(s)+1):
            for j in range(i):
                
                if dp[j] and searchTrie(s[j:i]):
                    dp[i]=True
                    break
                    
        return dp[-1]
        