import random

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def read_file(filename):
    with open(filename, 'r') as file:
        data = file.read().splitlines()
    return [int(value) for value in data]

def build_tree(values):
    root = Node(values[0])
    for value in values[1:]:
        insert_node(root, Node(value))
    return root

def insert_node(root, node):
    if root is None:
        root = node
    elif node.value < root.value:
        if root.left is None:
            root.left = node
        else:
            insert_node(root.left, node)
    else:
        if root.right is None:
            root.right = node
        else:
            insert_node(root.right, node)

def swap_children(node):
    if node is None:
        return
    if node.left is not None and node.right is not None:
        node.left, node.right = node.right, node.left
        swap_children(node.left)
        swap_children(node.right)
    elif node.left is not None:
        node.right = Node(random.randint(0, 100))
        node.left, node.right = node.right, node.left
        swap_children(node.left)
        swap_children(node.right)
    elif node.right is not None:
        node.left = Node(random.randint(0, 100))
        node.left, node.right = node.right, node.left
        swap_children(node.left)
        swap_children(node.right)

def find_node(root, value):
    if root is None or root.value == value:
        return root
    elif value < root.value:
        return find_node(root.left, value)
    else:
        return find_node(root.right, value)

def delete_node(root, value):
    if root is None:
        return root
    if value < root.value:
        root.left = delete_node(root.left, value)
    elif value > root.value:
        root.right = delete_node(root.right, value)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = find_min_node(root.right)
        root.value = temp.value
        root.right = delete_node(root.right, temp.value)
    return root

def find_min_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def print_tree(root):
    if root is not None:
        print_tree(root.left)
        print(root.value)
        print_tree(root.right)

def menu():
    values = read_file('tree_values.txt')
    root = build_tree(values)

    while True:
        print("Choose an option:")
        print("1. Add a node")
        print("2. Delete a node")
        print("3. Search for a node")
        print("4. Swap nodes")
        print("5. Print the tree")
        choice = input("Enter your choice: ")

        if choice == "1":
            value = int(input("Enter a value to add: "))
            insert_node(root, Node(value))
        elif choice == "2":
            value = int(input("Enter a value to delete: "))
            root = delete_node(root, value)
        elif choice == "3":
            value = int(input("Enter a value to search: "))
            node = find_node(root, value)
            if node is None:
                print("Node not found")
            else:
                print("Node found")
        elif choice == "4":
            swap_children(root)
        elif choice == "5":
            print_tree(root)

if __name__ == '__main__':
    menu()
