from typing import Optional, List

from tree.Invert_Binary_Tree import TreeNode
from tree.Lowest_Common_Ancestor_of_a_Binary_Search_Tree import create_tree


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue, result = [], []
        queue.append(root)
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)

        return result


if __name__ == '__main__':
    tree = create_tree()
    solution = Solution()
    print(solution.levelOrder(tree))
