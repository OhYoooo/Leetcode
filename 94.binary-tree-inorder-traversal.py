#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # no result
        if not root:
            return []
        self.result = []
        self.recursiveInOrderTraversal(root)
        return self.result
    
    def recursiveInOrderTraversal(self, node: TreeNode):
        if node.left != None:
            self.recursiveInOrderTraversal(node.left)
        self.result.append(node.val)
        if node.right != None:
            self.recursiveInOrderTraversal(node.right)


