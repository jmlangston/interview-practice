# given: a tree with integers as nodes
# task: write a function that prints all paths whose nodes add up to a given number

# note: this particular solution is recursive and uses depth-first, pre-order tree traversal

# TO DO: TEST THIS

class Node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def path_sum(root, my_sum, path):

    path.append(root.data)

    if root.data > my_sum:
        path.remove(path[-1])
    elif root.data == my_sum:
        if root.left is None and root.right is None:
            print path
        else:
            path.remove([-1])
    else:
        path_sum(root.left, (my_sum - root.data))
        path_sum(root.right, (my_sum - root.data))
        path.remove(path[-1])


# my_path = []
# path_sum()
