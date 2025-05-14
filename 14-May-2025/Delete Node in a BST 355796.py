# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def min_c(node):
            cur = node
            while cur.left:
                cur =  cur.left
            return cur

        def dfs_del(node, val):
            if not node:
                return node
            if val < node.val:
                node.left = dfs_del(node.left, val)
            elif val > node.val:
                node.right = dfs_del(node.right, val)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                temp = min_c(node.right)
                node.val = temp.val
                node.right = dfs_del(node.right, temp.val)
            

            return node
        return dfs_del(root, key)