class MaxSizeList(list):
    def __init__(self, max_size):
        self.max_size = max_size

    def append(self, element):
        super().append(element)
        if len(self) > self.max_size:
            self.pop(0)


# Example usage:
max_size_list = MaxSizeList(3)

max_size_list.append(1)
max_size_list.append(2)
max_size_list.append(3)

print("Current list:", max_size_list)  # Output: [1, 2, 3]

max_size_list.append(4)

print("Updated list:", max_size_list)  # Output: [2, 3, 4]
