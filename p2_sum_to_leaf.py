# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        """
        Time Complexity: O(n)
        Space Complexity: O(h)
        Did this code successfully run on Leetcode: Yes 

        Any problem you faced while coding this: No
        Your code here along with comments explaining your approach:
        The approach: 
            - we take currNum as local variable and result as the global variable
            - when we reach the leaf node we add the currNum to the result
            - we can add logic to any of the preorder, inorder, postorder
            - only thing we need to take care of is that we mutate the currNum
            before going to left and right 
        """      
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        self.helper(root, 0)
        return self.result
    
    def helper(self, root, currNum):
        #Base
        if root == None:
            return 

        #Logic
        currNum = currNum*10 + root.val
        self.helper(root.left, currNum)
        if root.left == None and root.right == None:
            self.result += currNum
        self.helper(root.right, currNum)
