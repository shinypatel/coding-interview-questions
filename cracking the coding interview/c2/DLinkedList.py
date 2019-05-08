class Node:
    def __init__(self, val=None):
        self.val = val
        self.prev, self.next = None, None


class DLinkedList:
    def __init__(self):
        self.head, self.tail = None, None
        self.len = 0

    def append(self, val):
        node = Node(val)
        if self.len == 0:
            self.head, self.tail = node, node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.len += 1

    def add(self, pos, val):
        node = Node(val)
        if pos == 0:
            self.head.prev = node
            node.next = self.head
            self.head = node
            self.len += 1
        elif self.len <= pos:
            self.append(val)
        else:
            count, curr = 0, self.head
            while count != pos - 1:
                curr = curr.next
                count += 1
            prev_node, next_node = curr, curr.next
            prev_node.next, next_node.prev = node, node
            node.prev, node.next = prev_node, next_node
            self.len += 1

    def remove(self, val, remove_all=False):  # q3
        curr = self.head
        while curr:
            if curr.val == val:
                if self.len == 1:
                    self.head, self.tail = None, None
                else:
                    if not curr.prev:
                        self.head = curr.next
                        self.head.prev = None
                    elif not curr.next:
                        self.tail = curr.prev
                        self.tail.next = None
                    else:
                        curr.prev.next = curr.next
                        curr.next.prev = curr.prev
                self.len -= 1
                if not remove_all:
                    break
            curr = curr.next

    def nth_to_last(self, n):   # q2
        ###########################
        # count, curr = 1, self.tail
        # while curr and count != n:
        #     curr = curr.prev
        #     count += 1
        ############################
        idx = self.len - 1 - (n - 1)
        count, curr = 0, self.head
        while curr and count != idx:
            curr = curr.next
            count += 1
        if count == idx and curr:
            return curr.val

    def find_starting_loop_val(self):   # q5
        values, start_val, curr = set(), None, self.head
        while curr:
            val = curr.val
            if val not in values:
                values.add(val)
            else:
                start_val = val
                break
            curr = curr.next
        return start_val

    def rm_dup_wo_buff(self):   # q1
        curr = self.head
        while curr:
            prev_node, node = curr, curr.next
            while node:
                if node.val == curr.val:
                    prev_node.next = node.next
                    if node.next:
                        node.next.prev = prev_node
                else:
                    prev_node = node
                node = node.next
            curr = curr.next

    def sum(self, list1, list2):    # q4
        carry, curr1, curr2 = 0, list1.head, list2.head
        while carry or curr1 or curr2:
            tmp = 0
            if curr1:
                tmp += curr1.val
                curr1 = curr1.next
            if curr2:
                tmp += curr2.val
                curr2 = curr2.next
            if carry:
                tmp += carry
            tmp = str(tmp)
            val = int(tmp[-1])
            if len(tmp) > 1:
                carry = int(tmp[:-1])
            else:
                carry = 0
            self.append(val)

    def print(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next


l1 = DLinkedList()
l2 = DLinkedList()
l3 = DLinkedList()

l1.append(3)
l1.append(1)
l1.append(5)

l2.append(5)
l2.append(9)
l2.append(2)

l3.sum(l1, l2)
l3.print()
