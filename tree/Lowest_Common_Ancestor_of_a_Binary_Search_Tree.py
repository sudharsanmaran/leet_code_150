from tree.Invert_Binary_Tree import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val <= root.val:
            self.lowestCommonAncestor(root.left, p, q)

    def bfs(self, root):
        pass


if __name__ == '__main__':
    # Create two identical binary trees for testing
    # Tree:
    #       6
    #    /     \
    #   2       8
    #  / \     /  \
    # 0   4   7    9
    #    / \
    #   3   5
    tree = TreeNode(6)
    tree.left = TreeNode(2)
    tree.right = TreeNode(8)
    tree.left.left = TreeNode(0)
    tree.left.right = TreeNode(4)
    tree.left.right.left = TreeNode(3)
    tree.left.right.right = TreeNode(5)
    tree.right.left = TreeNode(7)
    tree.right.right = TreeNode(9)

    solution = Solution()
    print(solution.lowestCommonAncestor(tree))
