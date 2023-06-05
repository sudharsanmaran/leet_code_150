from typing import Optional

from tree.Invert_Binary_Tree import TreeNode


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node_1, node_2):
            if not node_1 and not node_2:
                return True

            if node_1 is None or node_2 is None or node_1.val != node_2.val:
                return False

            return dfs(node_1.left, node_2.left) and dfs(node_1.right, node_2.right)
        return dfs(p, q)

    def is_sam_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        return True



if __name__ == '__main__':
    # Create two identical binary trees for testing
    # Tree 1:
    #     1
    #    / \
    #   2    3
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)

    # Tree 2:
    #     1
    #    / \
    #   2    3
    tree2 = TreeNode(1)
    tree2.left = TreeNode(2)
    tree2.right = TreeNode(3)

    # Create an instance of the Solution class
    solution = Solution()

    # Check if the two trees are the same
    is_same = solution.isSameTree(tree1, tree2)
    print("Are the trees the same?", is_same)
