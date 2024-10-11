class RedBlackTreeNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.color = 1


class RedBlackTree():
    def __init__(self):
        self.root = None


    def insert(self, value):
        insert_node = RedBlackTreeNode(value)
        if self.root == None:
            self.root = insert_node
            self.root.color = 2
        else:
            self.insert_help(insert_node, self.root)
            self.red_black_check_transfer(insert_node)
    def insert_help(self, insert_node, current):
        if current.value > insert_node.value:
            if current.left:
                self.insert_help(insert_node, current.left)
            else:
                current.left = insert_node
        elif current.value < insert_node.value:
            if current.right:
                self.insert_help(insert_node, current.right)
            else:
                current.right = insert_node
        else:
            return
        insert_node.parent = current


    def red_black_check_transfer(self, current):
        if self.root.color == 1:
            self.root.color = 2
        if current.color == 1:
            if current.parent.parent:
                if current.parent.parent.left == current.parent:
                    uncle = current.parent.parent.right
                else:
                    uncle = current.parent.parent.left
                if uncle is not None and uncle.color == 1:
                    current.parent.color = 2
                    uncle.color = 2
                    current.parent.parent.color = 1
                    self.red_black_check_transfer(current.parent.parent)

                elif uncle is None or uncle.color == 2:
                    if current == current.parent.left and current.parent == current.parent.parent.left:
                        self.right_rotate(current.parent.parent)
                        current.parent.color, current.parent.parent.color = current.parent.parent.color, current.parent.color
                    elif current == current.parent.right and current.parent == current.parent.parent.right:
                        self.left_rotate(current.parent.parent)
                        current.parent.color, current.parent.parent.color = current.parent.parent.color, current.parent.color
                    elif current == current.parent.right and current.parent == current.parent.parent.left:
                        self.left_rotate(current.parent)
                        self.right_rotate(current.parent.parent)
                    elif current == current.parent.left and current.parent == current.parent.parent.right:
                        self.right_rotate(current.parent)
                        self.left_rotate(current.parent.parent)
                        current.color, current.parent.parent.color = current.parent.parent.color, current.color


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



red_black_tree = RedBlackTree()

tree1 = red_black_tree
tree1.insert(10)

print(tree1.pre_order_traversal())

tree1.insert(12)

print(tree1.pre_order_traversal())

tree1.insert(5)

print(tree1.pre_order_traversal())

tree1.insert(15)

print(tree1.pre_order_traversal())

tree1.insert(7)

print(tree1.pre_order_traversal())

tree1.insert(2)

print(tree1.pre_order_traversal())

tree1.insert(6)

print(tree1.pre_order_traversal())

tree1.insert(20)

print(tree1.pre_order_traversal())

tree1.insert(30)

print(tree1.pre_order_traversal())

tree1.insert(40)

print(tree1.pre_order_traversal())

tree1.insert(50)

print(tree1.pre_order_traversal())


