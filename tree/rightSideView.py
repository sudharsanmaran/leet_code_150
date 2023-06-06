from collections import deque
from typing import Optional, List

from tree.Invert_Binary_Tree import TreeNode
from tree.Lowest_Common_Ancestor_of_a_Binary_Search_Tree import create_tree


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue, right_side_view_nodes = deque(), []
        queue.append(root)
        while queue:
            right_node = None
            level_length = len(queue)
            for _ in range(level_length):
                node = queue.popleft()

                if right_node is None:
                    right_node = node.val

                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            right_side_view_nodes.append(right_node)
        return right_side_view_nodes


if __name__ == '__main__':
    # Tree:
    #       6
    #    /     \
    #   2       8
    #  / \     /  \
    # 0   4   7    9
    #    / \
    #   3   5
    _tree = create_tree()
    sol = Solution()

    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(0)

    print(sol.rightSideView(_tree))
