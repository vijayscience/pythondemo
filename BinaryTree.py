class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def in_order_traverse(self):
        elements = []
        # its like descending Ascending order of elements.
        if self.left:
            elements += self.left.in_order_traverse()
        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traverse()

        return elements

    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        else:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()


def build_tree(elements):
    root = BinarySearchTree(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root


if __name__ == '__main__':
    # root = BinarySearchTree(5)
    # root.add_child(6)
    # root.add_child(2)
    numbers = [14, 5, 6, 7, 12, 15, 17, 34, 8, 9, 10, 24]
    print("Input Numbers ", numbers)
    # root = build_tree(numbers)
    # print(root.in_order_traverse())
    # print(root.search(34))
    # # print(root.search(35))

    # country = ["Belarus", "Australia", "Bulgaria", "Denmark", "Georgia", "Iceland", "Jordan"]
    # print("ALL ", country)
    # root = build_tree(country)
    # print(root.in_order_traverse())
    # print(root.search("Iceland"))
    # print(root.search("China"))
    delete_number = build_tree(numbers)
    delete_number.delete(10)
    print(delete_number.in_order_traverse())
