# given: a tree with numbers as nodes
# task: write a function that prints all paths whose nodes add up to a given number

# note: this particular solution is recursive and uses depth-first, pre-order tree traversal

# TO DO: TEST THIS


class Node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node(6)
node1 = Node(1)
node5 = Node(5)
node9 = Node(9)
node4 = Node(4)
node2 = Node(2)

root.left = node1
root.right = node4

node1.left = node5
node1.right = node9

node4.left = node2


def path_sum(root, my_sum, path):

    path.append(root.data)

    # print path

    if root.data > my_sum:
        path.remove(path[-1])
    elif root.data == my_sum:
        if root.left is None and root.right is None:
            print path
        else:
            path.remove([-1])
    else:
        path_sum(root.left, (my_sum - root.data), path)
        # path_sum(root.right, (my_sum - root.data), path)
        path.remove(path[-1])
        # print path


my_path = []
path_sum(root, 12, my_path)
