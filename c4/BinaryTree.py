class Node:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None

    def insert(self, v):
        if v <= self.val:
            if self.left:
                self.left.insert(v)
            else:
                self.left = Node(v)
        else:
            if self.right:
                self.right.insert(v)
            else:
                self.right = Node(v)

    def find(self, v):
        if v == self.val:
            return v
        elif v < self.val:
            if self.left:
                return self.left.find(v)
        else:
            if self.right:
                return self.right.find(v)

    def in_order_successor(self):
        if self.left:
            return self.left.in_order_successor()
        return self

    def print_in_order(self):   # left -> root -> right
        if self.left:
            self.left.print_in_order()
        print(self.val)
        if self.right:
            self.right.print_in_order()

    def print_pre_order(self):      # root -> left -> right
        print(self.val)
        if self.left:
            self.left.print_pre_order()
        if self.right:
            self.right.print_pre_order()

    def print_post_order(self):     # left -> right -> root
        if self.left:
            self.left.print_post_order()
        if self.right:
            self.right.print_post_order()
        print(self.val)


root = Node(4)
root.insert(3)
root.insert(6)
root.insert(1)
root.insert(5)
root.insert(2)

root.print_in_order()
