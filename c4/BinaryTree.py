from __future__ import division
import math


class Node:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.parent = None
        self.right = None

    def insert(self, v):
        if v <= self.val:
            if self.left:
                self.left.insert(v)
            else:
                self.left = Node(v)
                self.left.parent = self
        else:
            if self.right:
                self.right.insert(v)
            else:
                self.right = Node(v)
                self.right.parent = self

    def node(self, v):
        if v == self.val:
            return self
        elif v < self.val and self.left:
            return self.left.node(v)
        elif self.right:
            return self.right.node(v)

    def in_order_successor(self, v):   # q5
        node = self.node(v)
        successor = None
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            successor = node.val
        else:
            parent = node.parent
            while parent and (not parent.left or parent.left.val != node.val):
                node = node.parent
                parent = node.parent
            if parent:
                successor = parent.val
        return successor

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


def size(node):
    if not node:
        return 0
    return size(node.left) + size(node.right) + 1


def height(node):
    if not node:
        return 0
    return max(height(node.left), height(node.right)) + 1


def balanced(node):     # q1
    if not node:
        return True
    return balanced(node.left) and balanced(node.right) and \
           (abs(height(node.left) - height(node.right)) < 2)


def median(length):
    if length % 2 == 0:     # even
        return int(length / 2)
    else:   # odd
        return int(math.ceil(length / 2) - 1)


def binary_tree(arr):   # q3
    length = len(arr)
    idx = median(length)
    root = Node(arr[idx])
    left_half, right_half = arr[:idx], arr[idx + 1:]

    if len(left_half) > 1:
        root.left = binary_tree(left_half)
    elif len(left_half):
        root.left = Node(left_half[0])

    if len(right_half) > 1:
        root.right = binary_tree(right_half)
    elif len(right_half):
        root.right = Node(right_half[0])

    return root


arr = []
for i in range(6):
    arr.append(i)
bt = binary_tree(arr)
print('ht:', height(bt), '\n')
bt.print_in_order()
