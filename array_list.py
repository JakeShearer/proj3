# a List represents an array, a size, and a capacity
class List:
    def __init__(self, array, size, capacity):
        self.array = array # an array (a python built-in list)
        self.size = size # a number
        self.capacity = capacity # a number

    def __eq__(self, other):
        return (type(other) == List
                and self.array == other.array
                and self.size == other.size
                and self.capacity == other.capacity
                )

    def __repr__(self):
        return "List({!r}, {!r}, {!r})".format(self.array, self.size, self.capacity)
    
# => List
# returns an empty list
def empty_list():
    return List([], 0, 0)

# List int value => List
# adds a value to an List at a certain index
def add(list, index, value):
    if index < 0 or index > length(list):
        raise IndexError
    else:
        if list.capacity == 0:
            return List([value], 1, 1)
        else:
            if list.size == list.capacity:
                new_array = [None] * (2 * list.capacity)
                for i in range(list.capacity):
                    new_array[i] = list.array[i]
                new_array = add_element(List(new_array, list.size, 2*list.capacity), index, value)
                return List(new_array, list.size + 1, list.capacity * 2)
            else:
                new_array = add_element(list, index, value)
                return List(new_array, list.size+1, list.capacity)

# List int value => array
# adds a value to an array
def add_element(list,index,value):
    new_array = [None] * list.capacity
    for i in range(list.capacity):
        new_array[i] = list.array[i]
    temp = value
    for i in range(index, list.size+1):
        nexttemp = new_array[i]
        new_array[i] = temp
        temp = nexttemp
    return new_array

# List => int
# determines the length of a List
def length(list):
    return list.size

# List int => value
# determines the item at a certain spot in the list
def get(list, index):
    if index < 0 or index >= length(list):
        raise IndexError
    return list.array[index]

# List int value => List
# replaces the value at a specified index with a given value
def set(list, index, value):
    if index < 0 or index >= length(list):
        raise IndexError
    new_array = [None] * list.capacity
    for i in range(list.capacity):
        new_array[i] = list.array[i]
    new_array[index] = value
    return List(new_array, list.size, list.capacity)

# List int => List
# removes an element from a list and returns a tuple with the removed element and the resulting list
def remove(list, index):
    if index < 0 or index >= length(list):
        raise IndexError
    else:
        new_array = [None] * list.capacity
        for i in range(list.capacity):
            new_array[i] = list.array[i]
        element = get(list, index)
        new_array = remove_element(list, index)
        return element, List(new_array, list.size-1, list.capacity)

# List int => array
# removes an element at a given index in an array and returns the resulting array
def remove_element(list,index):
    new_array = [None] * list.capacity
    for i in range(list.capacity):
        new_array[i] = list.array[i]
    for i in range(index, list.size):
        if i == list.size-1:
            new_array[i] = None
        else:
            new_array[i] = new_array[i+1]
    return new_array

