from typing import Optional

from tree.Invert_Binary_Tree import TreeNode


class Solution:
    def isSubtree(self, root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
        if not sub_root:
            return True
        if not root:
            return False

        if self.is_same_tree(root, sub_root):
            return True

        return self.isSubtree(root.left, sub_root) or self.isSubtree(root.right, sub_root)

    def is_same_tree(self, node_1, node_2):
        if not node_1 and not node_2:
            return True

        if not node_1 or not node_2 or node_1.val != node_2.val:
            return False

        return self.is_same_tree(node_1.left, node_2.left) and self.is_same_tree(node_1.right, node_2.right)


if __name__ == '__main__':
    # Create two identical binary trees for testing
    # Tree 1:
    #     1
    #    / \
    #   2    3
    #  / \    \
    # 4   5    7
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)
    tree1.left.left = TreeNode(4)
    tree1.left.right = TreeNode(5)
    tree1.right.right = TreeNode(7)

    # Tree 2:
    #     2
    #    / \
    #   4   5
    tree2 = TreeNode(2)
    tree2.left = TreeNode(4)
    tree2.right = TreeNode(5)

    # Create an instance of the Solution class
    solution = Solution()

    # Check if the two trees are the same
    is_sub = solution.isSubtree(tree1, tree2)
    print("is tree2 is sub tree of tree?", is_sub)
