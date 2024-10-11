"""
           10
         /   \
        5     12
       / \     \
      2   7     15
         /
        6
"""
class TreeNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree():
    def __init__(self):
        self.root = None


    def insert_loop(self, value):
        insert_node = TreeNode(value)
        if self.root == None:
            self.root = insert_node
        else:
            current = self.root
            while True:
                if current.value > value:
                    if current.left == None:
                        current.left = insert_node
                        break
                    else:
                        current = current.left
                elif current.value < value:
                    if current.right == None:
                        current.right = insert_node
                        break
                    else:
                        current = current.right
                else:
                    return


    def insert(self, value):
        insert_node = TreeNode(value)
        if self.root == None:
            self.root = insert_node
        else:
            self.insert_help(insert_node, self.root)

    def insert_help(self, insert_node, current):
        if current.value > insert_node.value:
            if current.left == None:
                current.left = insert_node
            else:
                self.insert_help(insert_node, current.left)
        elif current.value < insert_node.value:
            if current.right == None:
                current.right = insert_node
            else:
                self.insert_help(insert_node, current.right)
        else:
            return

    def delete(self, value):
        if self.root == None:
            raise ValueError('This is an empty tree!')
        else:
            self.delete_help(value, self.root)

    def delete_help(self, value, current):
        if current.value == value and current == self.root:
            predecessor = self.find_inorder_predecessor(self.root)
            predecessor_value = predecessor.value
            self.delete(predecessor_value)
            self.root.value = predecessor_value

        elif current.value > value:
            if current.left:
                self.delete_help(value, current.left)

        elif current.value < value:
            if current.right:
                self.delete_help(value, current.right)

        if current.left:
            if current.left.value == value:
                if current.left.left is None and current.left.right is None:
                    current.left = None

                elif current.left.left is None:
                    current.left = current.left.right

                elif current.left.right is None:
                    current.left = current.left.left

                else:
                    predecessor = self.find_inorder_predecessor(current.left)
                    predecessor_value = predecessor.value
                    self.delete(predecessor_value)
                    current.left.value = predecessor_value

        if current.right:
            if current.right.value == value:
                if current.right.left is None and current.right.right is None:
                    current.right = None

                elif current.right.left is None:
                    current.right = current.right.right

                elif current.right.right is None:
                    current.right = current.right.left

                else:
                    predecessor = self.find_inorder_predecessor(current.right)
                    predecessor_value = predecessor.value
                    self.delete(predecessor_value)
                    current.right.value = predecessor_value



    def find_inorder_predecessor(self, node):
        if node:
            if node.left:
                return self.find_last_right_node(node.left)
            else:
                return node.left

    def find_last_right_node(self, current):
        if current.right:
            return self.find_last_right_node(current.right)
        else:
            return current

    def find_inorder_successor(self, node):
        if node:
            if node.right:
                return self.find_last_left_node(node.right)
            else:
                return node.right

    def find_last_left_node(self, current):
        if current.left:
            return self.find_last_left_node(current.left)
        else:
            return current


    def pre_order_traversal(self):
        """
        前序遍历中，按照以下顺序访问节点：根节点、左子树、右子树
        """
        output_list = []
        if self.root == None:
            return output_list
        else:
            return self.pre_order_traversal_help(self.root, output_list)

    def pre_order_traversal_help(self, current, output_list):
        if current:
            output_list.append(current.value)
            self.pre_order_traversal_help(current.left, output_list)
            self.pre_order_traversal_help(current.right, output_list)
        return output_list


    def pre_order_traversal_loop(self):
        output_list = []
        help_stack = [self.root]
        if self.root == None:
            return output_list
        else:
            while help_stack:
                current = help_stack.pop()
                output_list.append(current.value)
                if current.right:
                    help_stack.append(current.right)
                if current.left:
                    help_stack.append(current.left)
            return output_list

    def in_order_traversal(self):
        """
        #中序遍历中，按照以下顺序访问节点：左子树、根节点、右子树。输出一定是从小到大顺序排列！
        """
        output_list = []
        if self.root == None:
            return output_list
        else:
            return self.in_order_traversal_help(self.root, output_list)

    def in_order_traversal_help(self, current, output_list):
        if current:
            self.in_order_traversal_help(current.left, output_list)
            output_list.append(current.value)
            self.in_order_traversal_help(current.right, output_list)
        return output_list


    def post_order_traversal(self):
        """
        后序遍历中，按照以下顺序访问节点：左子树、右子树、根节点。
        """
        output_list = []
        if self.root == None:
            return output_list
        else:
            return self.post_order_traversal_help(self.root, output_list)

    def post_order_traversal_help(self, current, output_list):
        if current:
            self.in_order_traversal_help(current.left, output_list)
            self.in_order_traversal_help(current.right, output_list)
            output_list.append(current.value)
        return output_list


    def search(self, value):
        if self.root == None:
            raise ValueError('Empty Tree!')
        elif self.root.value == value:
            return True
        else:
            return self.search_help(value, self.root)

    def search_help(self, value, current):
        if current == None:
            return False
        if current.value == value:
            return True
        if current.value > value:
            return self.search_help(value, current.left)
        elif current.value < value:
            return self.search_help(value, current.right)


    def search_loop(self, value):
        if self.root == None:
            raise ValueError('Empty Tree!')
        else:
            help_stack = [self.root]
            while help_stack:
                current = help_stack.pop()
                if current.value == value:
                    return True
                elif current.value > value:
                    if current.left:
                        help_stack.append(current.left)
                elif current.value < value:
                    if current.right:
                        help_stack.append(current.right)
            return False


    def depth(self, value):
        if self.root == None:
            raise ValueError('Empty Tree!')
        elif self.root.value == value:
            return 0
        else:
            if self.depth_help(value, self.root, 0):
                return self.depth_help(value, self.root, 0)
            else:
                raise ValueError('This value is not in the tree!')

    def depth_help(self, value, current, depth):
        if current.value == value:
            return depth
        elif current.value > value:
            if current.left:
                return self.depth_help(value, current.left, depth+1)
        elif current.value < value:
            if current.right:
                return self.depth_help(value, current.right, depth+1)


    def height(self):
        if self.root == None:
            return None
        elif self.root.right == None and self.root.left == None:
            return 0
        else:
            return self.height_help(current = self.root, depth = 0, depth_list = [])

    def height_help(self, current, depth, depth_list):
        if current.left == None and current.right == None:
            depth_list.append(depth)
        else:
            if current.left:
                self.height_help(current.left, depth+1, depth_list)
            if current.right:
                (self.height_help(current.right, depth+1, depth_list))
        return max(depth_list)



bst=BinarySearchTree()

bst.insert(10)

bst.insert(12)

bst.insert(5)

bst.insert(15)

bst.insert(7)

bst.insert(2)

bst.insert(6)

print(bst.pre_order_traversal())

print(bst.pre_order_traversal_loop())

print(bst.in_order_traversal())

print(bst.post_order_traversal())

print(bst.search(6))

print(bst.search(1.345))

print(bst.search_loop(15))

print(bst.search_loop(1.345))

print(bst.depth(15))

print(bst.height())

bst.delete(10)

print(bst.pre_order_traversal())