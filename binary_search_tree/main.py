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
        new_node = TreeNode(value)
        if self.root == None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if current.value > value:
                    if current.left == None:
                        current.left = new_node
                        break
                    else:
                        current = current.left
                elif current.value < value:
                    if current.right == None:
                        current.right = new_node
                        break
                    else:
                        current = current.right
                else:   #不处理与树中已有元素重复的元素，直接返回
                    return


    def insert_recursion(self, value):
        new_node = TreeNode(value)
        if self.root == None:
            self.root = new_node
        else:
            self.insert_recursion_1(new_node, self.root)
    def insert_recursion_1(self, new_node, node):
        if node.value > new_node.value:
            if node.left == None:
                node.left = new_node
            else:
                self.insert_recursion_1(new_node, node.left)
        elif node.value < new_node.value:
            if node.right == None:
                node.right = new_node
            else:
                self.insert_recursion_1(new_node, node.right)


    def preorder_traversal(self):
        if self.root == None:
            return []
        else:
            return self.preorder_traversal_(node = self.root)

    def preorder_traversal_(self, node, traversal_list = None): #前序遍历中，按照以下顺序访问节点：根节点、左子树、右子树
        if traversal_list == None:
            traversal_list = []
        if node != None:
            traversal_list.append(node.value)
            self.preorder_traversal_(node.left, traversal_list)
            self.preorder_traversal_(node.right, traversal_list)
        return traversal_list


    def preorder_traversal_loop(self):
        traversal_list = []
        if self.root == None:
            return traversal_list
        stack = [self.root]
        while stack:
            node = stack.pop()
            traversal_list.append(node.value)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return traversal_list


    def inorder_traversal(self):  #中序遍历中，按照以下顺序访问节点：左子树、根节点、右子树。输出一定是从小到大顺序排列！
        if self.root == None:
            return []
        else:
            return self.inorder_traversal_(node = self.root)

    def inorder_traversal_(self, node, traversal_list=None):
        if traversal_list == None:
            traversal_list = []
        if node != None:  #基线条件为：node=None时，不执行代码，直接return
          #以下为递归条件（在达到基线条件前一直执行）
            self.inorder_traversal_(node.left, traversal_list)
            traversal_list.append(node.value)
            self.inorder_traversal_(node.right, traversal_list)
        return traversal_list


    def postorder_traversal(self):  #后序遍历中，按照以下顺序访问节点：左子树、右子树、根节点
        if self.root == None:
            return []
        else:
            return self.postorder_traversal_(node=self.root)

    def postorder_traversal_(self, node, traversal_list=None):
        if traversal_list == None:
            traversal_list = []
        if node != None:
            self.postorder_traversal_(node.left, traversal_list)
            self.postorder_traversal_(node.right, traversal_list)
            traversal_list.append(node.value)
        return traversal_list


    def search(self, value):
        if self.root == None:
            raise ValueError('Empty Tree!')
        elif self.root.value == value:
            return True
        else:
            return self.search_(node=self.root, value=value)
    def search_(self, node, value):
        if node == None:
            return False
        elif node.value == value:
            return True
        else:
            if node.value > value:
                return self.search_(node.left, value)
            else:
                return self.search_(node.right, value)

    def search_loop(self, value):
        if self.root == None:
            raise ValueError('Empty Tree!')
        elif self.root.value == value:
            return True
        else:
            stack = [self.root]
            while stack:
                current_node = stack.pop()
                if current_node.right:
                    if current_node.right.value == value:
                        return True
                    else:
                        stack.append(current_node.right)
                if current_node.left:
                    if current_node.left.value == value:
                        return True
                    else:
                        stack.append(current_node.left)
            return False


    def search_loop_another_version(self, value):
        if self.root == None:
            raise ValueError('Empty Tree!')
        elif self.root.value == value:
            return True
        else:
            stack = [self.root]
            while stack:
                current_node = stack.pop()
                if current_node.value == value:
                    return True
                elif current_node.value < value:
                    if current_node.right:
                        stack.append(current_node.right)
                else:
                    if current_node.left:
                        stack.append(current_node.left)
            return False


    def depth(self, value):
        if self.root == None:
            raise ValueError('Empty Tree!')
        if self.root.value == value:
            return 0
        else:
            return self.depth_(node=self.root, value=value)

    def depth_(self, node, value, index=0):
        if node.value != value:
            if node.value > value:
                return self.depth_(node = node.left, value=value, index = index + 1)
            else:
                return self.depth_(node=node.right, value=value, index= index + 1)
        return index


    def height(self):
        if self.root == None:
            return None
        elif self.root.right == None and self.root.left == None:
            return 0
        else:
            return max(self.leafs_depth(node=self.root, index=0, depth_list=[]))

    def leafs_depth(self, node, index, depth_list):
        if node.left == None and node.right == None:
            depth_list.append(index)
        if node.left != None:
            self.leafs_depth(node.left, index+1, depth_list)
        if node.right != None:
            self.leafs_depth(node.right, index+1, depth_list)
        return depth_list



bst=BinarySearchTree()

bst.insert_recursion(10)

bst.insert_recursion(12)

bst.insert_recursion(5)

bst.insert_recursion(15)

bst.insert_recursion(7)

bst.insert_recursion(2)

bst.insert_recursion(6)

print(bst.preorder_traversal())

print(bst.preorder_traversal_loop())

print(bst.inorder_traversal())

print(bst.postorder_traversal())

print(bst.search_loop(15))

print(bst.search_loop(1.345))

print(bst.search(6))

print(bst.search(1.345))

print(bst.search_loop_another_version(12))

print(bst.search_loop_another_version(1.345))

print(bst.depth(7))

print(bst.height())