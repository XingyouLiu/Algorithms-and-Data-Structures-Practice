class AVLTreeNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1
        self.parent = None


class AVLTree():
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if not node:
            return 0
        return node.height


    def insert(self, value):
        insert_node = AVLTreeNode(value)
        if self.root == None:
            self.root = insert_node
        else:
            self.insert_help(insert_node, self.root)

    def insert_help(self, insert_node, current):
        if current.value > insert_node.value:
            if current.left:
                self.insert_help(insert_node, current.left)
            else:
                current.left = insert_node
                insert_node.parent = current
        elif current.value < insert_node.value:
            if current.right:
                self.insert_help(insert_node, current.right)
            else:
                current.right = insert_node
                insert_node.parent = current
        else:
            return
        current.height = 1 + max(self.get_height(current.left), self.get_height(current.right))
        self.balance_check(current)


    def delete(self, value):
        if self.root == None:
            raise ValueError('This is an empty tree!')
        else:
            self.delete_help(value, self.root)

    def delete_help(self, value, current):
        if current.value > value:
            if current.left:
                self.delete_help(value, current.left)

        elif current.value < value:
            if current.right:
                self.delete_help(value, current.right)

        elif current.value == value:
            if current.left is None and current.right is None:
                if current == current.parent.left:
                    current.parent.left = None
                elif current == current.parent.right:
                    current.parent.right = None
                current.parent.height = 1 + max(self.get_height(current.parent.left), self.get_height(current.parent.right))
                self.balance_check(current.parent)

            elif current.left is None:
                if current.parent.left == current:
                    current.parent.left = current.right
                    current.parent.height = 1 + max(self.get_height(current.parent.left),
                                                    self.get_height(current.parent.right))
                    self.balance_check(current.parent.left)
                elif current.parent.right == current:
                    current.parent.right = current.right
                    current.parent.height = 1 + max(self.get_height(current.parent.left),
                                                    self.get_height(current.parent.right))
                    self.balance_check(current.parent.right)

            elif current.right == None:
                if current.parent.left == current:
                    current.parent.left = current.left
                    current.parent.height = 1 + max(self.get_height(current.parent.left),
                                                    self.get_height(current.parent.right))
                    self.balance_check(current.parent.left)
                elif current.parent.right == current:
                    current.parent.right = current.left
                    current.parent.height = 1 + max(self.get_height(current.parent.left),
                                                    self.get_height(current.parent.right))
                    self.balance_check(current.parent.right)

            else:
                if self.get_height(current.left) > self.get_height(current.right):
                    predecessor = self.find_inorder_predecessor(current)
                    predecessor_value = predecessor.value
                    self.delete(predecessor_value)
                    current.value = predecessor_value
                    current.height = 1 + max(self.get_height(current.left),
                                                        self.get_height(current.right))
                    self.balance_check(current)

                else:
                    successor = self.find_inorder_successor(current)
                    successor_value = successor.value
                    self.delete(successor_value)
                    current.value = successor_value
                    current.height = 1 + max(self.get_height(current.left),
                                             self.get_height(current.right))
                    self.balance_check(current)




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



    def get_balance_factor(self, node):
        left_height = node.left.height if node.left else 0
        right_height = node.right.height if node.right else 0
        return left_height - right_height


    def balance_check(self, node):
        current = node
        if self.get_balance_factor(node) > 1:
            if self.get_balance_factor(node.left) > 0:
                current = self.right_rotate(node)
            elif self.get_balance_factor(node.left) < 0:
                current = self.left_right_rotate(node)
        elif self.get_balance_factor(node) < -1:
            if self.get_balance_factor(node.right) < 0:
                current = self.left_rotate(node)
            elif self.get_balance_factor(node.right) > 0:
                current = self.right_left_rotate(node)
        return current


    def right_rotate(self, node):
        new_root = node.left
        if node.parent:
            new_root.parent = node.parent
            if node.parent.right == node:
                node.parent.right = new_root
            elif node.parent.left == node:
                node.parent.left = new_root
        else:
            self.root = new_root
        original_left_right_child = new_root.right
        node.left = original_left_right_child
        if original_left_right_child:
            original_left_right_child.parent = node
        new_root.right = node
        node.parent = new_root
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        return new_root


    def left_rotate(self, node):
        new_root = node.right
        if node.parent:
            new_root.parent = node.parent
            if node.parent.right == node:
                node.parent.right = new_root
            elif node.parent.left == node:
                node.parent.left = new_root
        else:
            self.root = new_root
        original_right_left_child = new_root.left
        node.right = original_right_left_child
        if original_right_left_child:
            original_right_left_child.parent = node
        new_root.left = node
        node.parent = new_root
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        return new_root


    def left_right_rotate(self, node):
        new_left_child_root = self.left_rotate(node.left)
        node.left = new_left_child_root
        new_root = self.right_rotate(node)
        return new_root


    def right_left_rotate(self, node):
        new_right_child_root = self.right_rotate(node.right)
        node.right = new_right_child_root
        new_root = self.left_rotate(node)
        return new_root


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


    def search(self, value):
        if self.root == None:
            raise ValueError('Empty Tree!')
        elif self.root.value == value:
            return self.root
        else:
            return self.search_help(value, self.root)

    def search_help(self, value, current):
        if current == None:
            return False
        if current.value == value:
            return current
        if current.value > value:
            return self.search_help(value, current.left)
        elif current.value < value:
            return self.search_help(value, current.right)


    def get_node_height_left_right_parent(self, value):
        node = self.search(value)
        if node.left and node.right:
            return node.height, node.left.value, node.right.value, node.parent.value
        elif node.left is None and node.right is None:
            return node.height, 0, 0, node.parent.value
        elif node.left:
            return node.height, node.left.value, 0, node.parent.value
        elif node.right:
            return node.height, 0, node.right.value, node.parent.value


avl_tree = AVLTree()

avl_tree.insert(10)

print(avl_tree.pre_order_traversal())

avl_tree.insert(12)

print(avl_tree.pre_order_traversal())

avl_tree.insert(5)

print(avl_tree.pre_order_traversal())

avl_tree.insert(15)

print(avl_tree.pre_order_traversal())

avl_tree.insert(7)

print(avl_tree.pre_order_traversal())

avl_tree.insert(2)

print(avl_tree.pre_order_traversal())

avl_tree.insert(6)

print(avl_tree.pre_order_traversal())

avl_tree.insert(20)

print(avl_tree.pre_order_traversal())

avl_tree.insert(30)

print(avl_tree.pre_order_traversal())

avl_tree.insert(40)

print(avl_tree.pre_order_traversal())

avl_tree.insert(50)

print(avl_tree.pre_order_traversal())

print(avl_tree.get_node_height_left_right_parent((7)))

avl_tree.delete(10)

print(avl_tree.pre_order_traversal())