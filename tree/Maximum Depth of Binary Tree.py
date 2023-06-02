from typing import Optional

from tree.Invert_Binary_Tree import TreeNode, create_binary_tree

"""approach:
1. traverse every node of the tree and maintain level/depth counter
t O(n) / s O(1)"""


class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # iterative sol
    def max_depth(self, root: Optional[TreeNode]) -> int:
        """ use stack for dfs pre-order traversal"""
        if not root:
            return 0
        # have to store depth for every node
        stack, depth = [(root, 1)], 0
        while stack:
            root, cur_depth = stack.pop()
            depth = max(depth, cur_depth)
            if root.left:
                stack.append((root.left, cur_depth + 1))
            if root.right:
                stack.append((root.right, cur_depth + 1))
        return depth

    def max_depth_1(self, root: Optional[TreeNode]) -> int:
        """iterative dfs in-order traversal"""
        if not root:
            return 0

        stack, max_depth, depth = [], 0, 1
        while stack or root:
            # reach left most node
            while root:
                stack.append((root, depth))
                root = root.left
                depth += 1

            root, depth = stack.pop()
            max_depth = max(depth, max_depth)
            root = root.right
            depth += 1

        return max_depth


# use queue for BFS traversal while iteration

if __name__ == '__main__':
    obj = Solution()
    print(obj.max_depth_1(create_binary_tree()))
