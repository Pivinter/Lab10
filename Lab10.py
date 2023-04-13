import random

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def add_node(root, value):
    if root is None:
        return Node(value)
    else:
        if value < root.value:
            root.left = add_node(root.left, value)
        else:
            root.right = add_node(root.right, value)
    return root

def find_node(root, value):
    if root is None or root.value == value:
        return root

    if value < root.value:
        return find_node(root.left, value)
    else:
        return find_node(root.right, value)

def remove_node(root, value):
    if root is None:
        return root

    if value < root.value:
        root.left = remove_node(root.left, value)
    else:
        if value > root.value:
            root.right = remove_node(root.right, value)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            min_larger_node = find_min(root.right)
            root.value = min_larger_node.value
            root.right = remove_node(root.right, min_larger_node.value)

    return root

def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def build_tree_from_file(filename):
    with open(filename, 'r') as file:
        values = [int(value.strip()) for value in file.readlines()]
    root = None
    for value in values:
        root = add_node(root, value)
    return root

def swap_children(node):
    if node is None:
        return

    if node.left is not None and node.right is not None:
        node.left.value, node.right.value = node.right.value, node.left.value

    swap_children(node.left)
    swap_children(node.right)

def add_random_child(node):
    if node is None:
        return

    if node.left is None and node.right is not None:
        node.left = Node(random.randint(1, 100))
    elif node.left is not None and node.right is None:
        node.right = Node(random.randint(1, 100))

    add_random_child(node.left)
    add_random_child(node.right)

def print_tree(node, indent=0):
    if node is not None:
        print_tree(node.left, indent + 4)
        print(" " * indent + str(node.value))
        print_tree(node.right, indent + 4)



root = build_tree_from_file('tree_values.txt')
swap_children(root)
add_random_child(root)
print("Оберіть операцію:")
print("1. Додати вузол")
print("2. Видалити вузол")
print("3. Знайти вузол")
print("4. Показати дерево")
print("5. Обміняти вузли")
print("6. Завершити програму")

while True:
        choice = input("Введіть номер операції: ")

        if choice == '1':
            value = int(input("Введіть значення вузла для додавання: "))
            root = add_node(root, value)
            print("Вузол успішно додано.")
        elif choice == '2':
            value = int(input("Введіть значення вузла для видалення: "))
            root = remove_node(root, value)
            print("Вузол успішно видалено.")
        elif choice == '3':
            value = int(input("Введіть значення вузла для пошуку: "))
            node = find_node(root, value)
            if node is None:
                print("Вузол не знайдено.")
            else:
                print("Вузол знайдено.")
        elif choice == '4':
            print("Бінарне дерево:")
            print_tree(root)
        elif choice == '5':
            swap_children(root)
            print("Вузли успішно обмінено.")
        elif choice == '6':
            print("Завершення програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")