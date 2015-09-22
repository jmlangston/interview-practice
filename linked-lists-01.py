# define Node and Linked_List classes

class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_List(object):

    def __init__(self, head):
        self.head = head


def print_nodes(linked_list):
    """Prints each node in a linked list (with or without a loop)."""

    current_node = linked_list.head

    nodes_printed = set([])

    while current_node not in nodes_printed:
        print current_node.data
        nodes_printed.add(current_node)
        current_node = current_node.next


# takes in: linked list
# returns: True or False depending on if there is a loop in the linked list

def has_loop_1(linked_list):
    """Returns True if the linked list has a loop and False if it doesn't."""

    # using a set or dict instead of a list reduces runtime
    nodes_visited = set([])

    current_node = linked_list.head

    while current_node.next is not None:
        if current_node not in nodes_visited:
            nodes_visited.add(current_node)
            current_node = current_node.next
        else:
            return True

    return False


def has_loop_2(linked_list):
    """Uses 'the tortise and the hare' approach to determine presence of a loop in the linked list. Returns True or False accordingly."""

    tortise = linked_list.head
    hare = linked_list.head

    while tortise != hare and tortise != linked_list.head:
        tortise = tortise.next
        hare = hare.next.next

    return False


# other ways to check for a loop with less space cost:
# keep track on the Node whether or not it has been visited
# use two pointers, "tortise" advances one node and "hare" advances two nodes


###################################

# for the ease of testing in the console
# a linked list with a loop

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node3

loop_ll = Linked_List(node1)


# a linked list without a loop

node_a = Node('a')
node_b = Node('b')
node_c = Node('c')

node_a.next = node_b
node_b.next = node_c

my_ll = Linked_List(node_a)

###################################

# method calls

# print_nodes(loop_ll)

# has_loop(loop_ll)

###################################

# more practice

# takes in: linked list
# returns: head of a new reversed linked list

# def reverse_ll(ll):
