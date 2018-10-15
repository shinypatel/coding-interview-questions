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

    def find_node(self, v):
        if v == self.val:
            return self
        elif v < self.val and self.left:
            return self.left.find_node(v)
        elif self.right:
            return self.right.find_node(v)

    def in_order_successor(self, v):  # q5
        node = self.find_node(v)
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

    def print_pre_order_traversal(self):  # root -> left -> right
        print(self.val)
        if self.left:
            self.left.print_pre_order_traversal()
        if self.right:
            self.right.print_pre_order_traversal()


def size(node):
    if not node:
        return 0
    return size(node.left) + size(node.right) + 1


def height(node):
    if not node:
        return -1
    return max(height(node.left), height(node.right)) + 1


def balanced(node):  # q1
    if not node:
        return True
    return balanced(node.left) and balanced(node.right) and \
           (abs(height(node.left) - height(node.right)) < 2)


def median(length):
    if length % 2 == 0:  # even
        return int(length / 2)
    else:  # odd
        return int(math.ceil(length / 2) - 1)


def binary_tree(arr):  # q3
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


''' nodes at same depth can have diff heights
    https://stackoverflow.com/questions/2603692/what-is-the-difference-between-tree-depth-and-height '''


def depth(node, d=-1):  # tail recursion
    if not node:
        return d
    d += 1
    return max(depth(node.left, d), depth(node.right, d))


def depth_lists(q, depths):  # q4
    d = []  # nodes at depth d
    node = q.pop(0)
    while node:
        d.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
        node = q.pop(0)

    if len(q):
        q.append(None)  # separate depths by None in queue
        depths = depth_lists(q, depths)

    depths.insert(0, d)
    return depths


def in_order_traversal(node, order=None):  # left -> root -> right
    if order is None:
        order = []

    if node.left:
        order = in_order_traversal(node.left, order)
    order.append(node.val)
    if node.right:
        order = in_order_traversal(node.right, order)
    return order


def post_order_traversal(node, order=None):  # left -> right -> root
    if order is None:
        order = []

    if node.left:
        order = post_order_traversal(node.left, order)
    if node.right:
        order = post_order_traversal(node.right, order)
    order.append(node.val)
    return order


def least_common_ancestor(root, v1, v2):  # q6
    in_order = in_order_traversal(root)
    post_order = post_order_traversal(root)

    i1, i2 = sorted([in_order.index(v1), in_order.index(v2)])
    relatives = in_order[i1:i2 + 1]

    for v in reversed(post_order):
        if v in relatives:
            return v


def list2str(l):
    return ''.join(str(el) for el in l)


def sub_tree(t1, t2):  # q7
    if list2str(in_order_traversal(t2)) in \
            list2str(in_order_traversal(t1)):
        if list2str(post_order_traversal(t2)) in \
                list2str(post_order_traversal(t1)):
            return True
    return False


def k_sum_path(node, k, path=None):     # q8
    if path is None:
        path = []
        if node.left:
            k_sum_path(node.left, k)
        if node.right:
            k_sum_path(node.right, k)

    j = sum(path)
    if j + node.val <= k:
        path.append(node.val)
        if k - (j + node.val):
            if node.left:
                # pass-by-value
                # because default is pass-by-reference
                k_sum_path(node.left, k, path[:])
            if node.right:
                k_sum_path(node.right, k, path[:])
        else:
            print(path)


bt = Node(4)
bt.insert(3)
bt.insert(6)
bt.insert(1)
bt.insert(5)
bt.insert(2)

k_sum_path(bt, 4)
