class MaxSizeList:

    def __init__(self, max_size):
        self.max_size = max_size
        self.internal_list = []

    def push(self, element):
        if len(self.internal_list) == self.max_size:
            self.internal_list.pop(0)  # Remove the first element if the list is full
        self.internal_list.append(element)

    def get_list(self):
        return self.internal_list


max_size_list = MaxSizeList(3)

max_size_list.push(1)
max_size_list.push(2)
max_size_list.push(3)

print("Current list:", max_size_list.get_list())  # Output: [1, 2, 3]

max_size_list.push(4)

print("Updated list:", max_size_list.get_list())  # Output: [2, 3, 4]
