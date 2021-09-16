class Solution:
    def topView(self,root):
        
        import sys
        sys.setrecursionlimit(10**6)
        
        global dx 
        dx = dict()
        result = []
        
        self.dfs(root,0,0) # calling with horizontal distance = 0
        
        for val in sorted(dx.keys()):
            result.append(dx[val][0])
            
        return result
        
    def dfs(self,root,HD,level):
        
        if not root:
            return 
        
        global dx
        
        if HD not in dx:
            dx[HD] = [root.data,level] 
        
        
        if level < dx[HD][1]: # if encounter a upper level then replace.
            dx[HD] = [root.data,level]
            
        self.dfs(root.left,  HD - 1,level + 1)
        self.dfs(root.right, HD + 1,level + 1) 