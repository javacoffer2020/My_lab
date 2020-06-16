class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __repr__(self):
        return str(self.data)


def is_cycle(head):
    p1 = head
    p2 = head
    while p2 is not None and p2.next is not None:
        p1 = p1.next
        p2 = p2.next.next
        if p1 == p2:
            return True
    return False


def cycle_length(head):
    p1 = head
    p2 = head
    length = 0
    while p2 is not None and p2.next is not None:
        p1 = p1.next
        p2 = p2.next.next
        if p1 == p2:
            p1 = p1.next
            p2 = p2.next.next
            length += 1
            while p1 != p2:
                p1 = p1.next
                p2 = p2.next.next
                length += 1
            break
    return length


def cycle_point(head):
    p1 = head
    p2 = head
    while p2 is not None and p2.next is not None:
        p1 = p1.next
        p2 = p2.next.next
        if p1 == p2:
            p1 = head
            while p1 != p2:
                p1 = p1.next
                p2 = p2.next
            return p1
    return None

node1 = Node(5)
node2 = Node(3)
node3 = Node(7)
node4 = Node(2)
node5 = Node(6)
node6 = Node(8)
node7 = Node(1)


node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node4

print(is_cycle(node1))
print(cycle_length(node1))
print(cycle_point(node1))