import random

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None 

class BST:

    def __init__(self, elements=[]):
        self._root = None 
        for element in elements:
            self.add(element)

    def add(self, value):
        if self._root is None:
            self._root = Node(value)
        else:
            self._add(self._root, value)

    def _add(self, node, value):
        if value == node.value:
            return
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._add(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._add(node.right, value)

    def count(self):
        return self._count(self._root)

    def _count(self, node):
        if node is None:
            return 0
        return 1 + self._count(node.left) + self._count(node.right)
  
    def search(self, value):
        return self._search(self._root, value)
    
    def _search(self, node, value):
        if node is None:
            return None 
        if node.value == value:
            return node 
        if value < node.value:
            if node.left is None:
                return None 
            self._search(node.left, value)
        else:
            if node.right is None:
                return None
            self._search(node.right, value)
    
    def search_min(self):
        return self._search_min(self._root)
    
    def _search_min(self, node):
        if node is None:
            return None
        while node.left is not None:
            node = node.left 
        return node.value 

    def search_max(self):
        return self._search_max(self._root)
    
    def _search_max(self, node):
        if node is None:
            return None
        # while node.right is not None:
        #     node = node.right 
        # return node.value 

        if node.right is None:
            return node.value 
        return self._search_max(node.right)
    
    def inorder(self):
        return self._inorder(self._root)

    def _inorder(self, node):
        if node is None:
            return []

        stack = []
        result = []
        while node is not None or stack != []:
            while node is not None:
                stack.append(node)
                node = node.left 
            node = stack.pop()
            result.append(node.value)
            node = node.right 
        return result 

    def preorder(self):
        return self._preorder(self._root)

    def _preorder(self, node):
        if node is None:
            return []

        stack = [node]
        result = []

        while stack != []:
            node = stack.pop()
            result.append(node.value)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

        return result  

if __name__ == '__main__':
    data = [random.randint(0, 100) for _ in range(15)]
    print("input", data)
    tree = BST(data)
    print("inorder", tree.inorder())
    print("preorder", tree.preorder())
    print("count", tree.count())
    for n in [random.randint(0, 100) for _ in range(3)]:
        node = tree.search(n)
        if node is not None:
            print(n, "Found")
        else:
            print(n, "Not found")
    
    print("min", tree.search_min())
    print("max", tree.search_max())