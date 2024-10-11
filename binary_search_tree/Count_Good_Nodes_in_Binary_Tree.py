def goodNodes_recursion(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """

    def DFS_find(current, max_in_coming_path, num):
        if current.val >= max_in_coming_path:
            max_in_coming_path = current.val
            num += 1
        if current.left:
            num = DFS_find(current.left, max_in_coming_path, num)
        if current.right:
            num = DFS_find(current.right, max_in_coming_path, num)
        return num

    return DFS_find(root, float('-inf'), 0)


def goodNodes_loop(self, root):
    max_in_coming_path = float('-inf')
    num = 0
    stack = [(root, max_in_coming_path)]  # 每个元组中的max_in_path存储从根节点到元组中节点的parent node的路径上的最大节点值
    while stack:
        (node, max_in_coming_path) = stack.pop()
        node_val = node.val
        if node_val >= max_in_coming_path:
            max_in_coming_path = node_val
            num += 1
        if node.right:
            stack.append((node.right, max_in_coming_path))
        if node.left:
            stack.append((node.left, max_in_coming_path))

    return num