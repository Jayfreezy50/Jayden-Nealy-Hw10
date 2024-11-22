# Jayden
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.value:
        root.left = insert(root.left, key)

    else:
        root.right = insert(root.right, key)

    return root

def inputTree():
    values = list(map(int, input("Enter the values, separated by spaces: ").split()))
    root = None

    for value in values:
        root = insert(root, value)

    return root

def sumOfLargest(root, k):
    count = 0
    result_sum = 0

    def reverseInorder(node):
        nonlocal count, result_sum
        if node is None or count >= k:
            return

        reverseInorder(node.right)

        if count < k:
            count += 1
            result_sum += node.value
        reverseInorder(node.left)
    reverseInorder(root)

    return result_sum

def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.value, end=" ")
        printInorder(root.right)

if __name__ == "__main__":
    root = inputTree()

    print("In-order traversal:")
    printInorder(root)
    print()

    k = int(input("Enter the value of k: "))
    sum_k_largest = sumOfLargest(root, k)
    print(f"The sum of elements greater than or equal to {k} and the largest element is: {sum_k_largest}")
