from collections import deque

from tree.Invert_Binary_Tree import TreeNode

"""approach:
1. traverse binary tree until we find the split of two given nodes. t => O(log n)
1.1 when ever the split occur that's our least common ancestor

edge case:
1. what if node node itself one of the given two nodes
    => then node node must be LCA
"""


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root.val

    def bfs(self, root):
        if not root:
            return []
        node_values = []
        total_sum = 0
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            node_values.append(node.val)
            total_sum += node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return node_values


def create_tree():
    tree = TreeNode(6)
    tree.left = TreeNode(2)
    tree.right = TreeNode(10)
    tree.left.left = TreeNode(0)
    tree.left.right = TreeNode(4)
    tree.left.right.left = TreeNode(3)
    tree.left.right.right = TreeNode(5)
    tree.right.left = TreeNode(7)
    tree.right.right = TreeNode(11)
    tree.right.left.right = TreeNode(8)
    return tree


if __name__ == '__main__':
    # Tree:
    #       6
    #    /     \
    #   2       10
    #  / \     /  \
    # 0   4   7    11
    #    / \   \
    #   3   5    8
    _tree = create_tree()

    solution = Solution()
    print(solution.lowestCommonAncestor(_tree, _tree.right.left, _tree.right.right))
