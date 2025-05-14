# Problem:  Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def insert(node, key):
            if not node:
                return TreeNode(key)
            if  key < node.val:
                node.left = insert(node.left, key)
            else:
                node.right = insert(node.right, key)
            return node
        
        return insert(root, val)
        