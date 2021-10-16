
import random    

class TreeNode:

    def __init__(self, value):
        self.value = value 
        self.left = None
        self.right = None 


    def add(self, value):
        if self.value == value:
            return
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.add(value)
        elif value > self.value:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.add(value)

    def search(self, value):
        if self.value == value:
            return True

        if value < self.value:
            if self.left is None:
                return False
            return self.left.search(value)
        if value > self.value:
            if self.right is None:
                return False
            return self.right.search(value)

    def search_min(self):
        if not self.left:
            return self.value 
        return self.left.search_min() 
        
    def search_max(self):
        if not self.right:
            return self.value
        return self.right.search_max() 

    def search_min_iter(self):
        while self.left:
            self = self.left
        return self.value
    
    def search_max_iter(self):
        while self.right:
            self = self.right
        return self.value

        
    def inorder(self):
        result = []
        if self.left:
            result += self.left.inorder()
        result.append(self.value) 
        if self.right:
            result += self.right.inorder()
        
        return result

    def preorder(self):
        result = [self.value] 
        if self.left:
            result += self.left.inorder()
        if self.right:
            result += self.right.inorder()
        
        return result

    def preorder_iter(self):
        root = self
        stack = [root]
        result = []
        while stack != []:
            root = stack.pop()
            result.append(root.value)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return result

    
    def inorder_iter(self):
        result = []
        stack = []
        root = self
        while root is not None or stack != []:
            while root is not None:
                stack.append(root)
                root = root.left 
            root = stack.pop()
            result.append(root.value)
            root = root.right 
        return result


if __name__ == '__main__':
    numbers = [random.randint(0, 100) for _ in range(15)]
    print(numbers)
    tree = TreeNode(numbers[0])
    for i in numbers[1:]:
        tree.add(i)
    print("inorder", tree.inorder())
    print("preorder", tree.preorder())
    print("preorder iter", tree.preorder_iter())
    for n in [random.randint(0, 100) for _ in range(3)]:
        print(n, tree.search(n))
    
    print("min", tree.search_min_iter())
    print("max", tree.search_max_iter())
    """
    import timeit
    print("Traverse recursion", timeit.timeit("tree.inorder()", globals=globals()))
    print("Traverse iterative", timeit.timeit("tree.inorder_iter()", globals=globals()))

    print("Search min recursion", timeit.timeit("tree.search_min()", globals=globals()))
    print("Search min iterative", timeit.timeit("tree.search_min_iter()", globals=globals())) """
    
