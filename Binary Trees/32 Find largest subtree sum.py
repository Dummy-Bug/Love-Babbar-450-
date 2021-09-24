# Find largest subtree sum in a tree

def largestSubtree(root):
    
    if not root:
        return 
    
    global max_sum 
    max_sum = float("-inf")
    
    largest_subtree(root,0)
    
    return max_sum
    
def largest_subtree(root,curr_sum):
    
    if not root:
        return 0
    
    left,right = 0,0
    
    if root.left:
        left  = self.largest_subtree(root.left,curr_sum)
        
    if root.right:
        right = self.largest_subtree(root.right,curr_sum)
        
    curr_sum = left + right + root.val
    
    global max_sum
    max_sum = max(max_sum,curr_sum)
    
    return curr_sum
        