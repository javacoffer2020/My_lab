class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def create_binary_tree(input_list=[]):
    if input_list is None or len(input_list) == 0:
        return None
    data = input_list.pop(0)
    if data is None:
        return None
    node = TreeNode(data)
    node.left = create_binary_tree(input_list)
    node.right = create_binary_tree(input_list)
    return node


def pre_order_traversal(node):
    """
    前序遍历
    :param node：二叉树节点
    """
    if node is None:
        return

    print(node.data,end=' ')
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)
    return node


def in_order_traversal(node):
    """
    中序遍历
    :param node：二叉树节点
    """
    if node is None:
        return

    in_order_traversal(node.left)
    print(node.data,end=' ')
    in_order_traversal(node.right)
    return node


def post_order_traversal(node):
    """
    后序遍历
    :param node: 二叉树节点
    """
    if node is None:
        return

    post_order_traversal(node.left)
    post_order_traversal(node.right)
    print(node.data,end=' ')
    return node


def pre_order_traversal_with_stack(node):
    stack = []
    while node is not None or len(stack) > 0:
        while node is not None:
            print(node.data,end=' ')
            stack.append(node)
            node = node.left
        if len(stack) > 0:
            node = stack.pop()
            node = node.right


def level_order_traversal(node):
    from queue import Queue
    queue = Queue()
    queue.put(node)
    while not queue.empty():
        node = queue.get()
        print(node.data,end=' ')
        if node.left is not None:
            queue.put(node.left)
        if node.right is not None:
            queue.put(node.right)


my_input_list = list([3,2,9,None,None,10,None,None,8,None,4])
root = create_binary_tree(my_input_list)
print("前序遍历：",end='')
pre_order_traversal(root)
print("中序遍历：",end='')
in_order_traversal(root)
print("后续遍历：",end='')
post_order_traversal(root)

print("非递归前序遍历：",end='')
pre_order_traversal_with_stack(root)

print("广度遍历：", end='')
level_order_traversal(root)