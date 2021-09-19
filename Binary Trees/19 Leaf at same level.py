class Solution:
    def check(self, root):
        
        global result 
        result = True
        
        self.helper(root)
        return result
        
    def helper(self,root):
        
        from collections import deque
        
        q = deque()
        q.append(root)
        flag = -1
        level = 0
        
        global result
        
        
        while q:
            
            for _ in range(len(q)):
                
                node = q.popleft()
                    
                if node.left:
                    q.append(node.left)
                        
                if node.right:
                    q.append(node.right)
                        
                if not node.left and not node.right:
                        
                    if flag == -1:
                        flag = level
                        
                    elif flag != level:
                        result = False
                        return False
            
            level = level + 1
        return result