import unittest

# represents a list implemented as an array
class ArrayList():
    def __init__(self, array, len):
        self.array = array
        self.len = len

    def __repr__(self):
        return "ArrayList(%r, %r)" % (self.array, self.len)

    def __eq__(self, other):
        return ((type(other) == ArrayList)
        and (self.array == other.array)
        and (self.len == other.len)
        )

    def __ne__(self, other):
        return (not (other == self))

# the initial size of an ArrayList
init_size = 5

# the amount by which the size of an ArrayList is multiplied
size_incr_factor = 2

# create a new empty ArrayList
def make_empty():
    return ArrayList([None] * init_size, 0)

# return the length of an ArrayList
def length(arr):
    return arr.len

# add an element to the end of an ArrayList
def add_to_end(arr,new_elt):
    maybe_extend_array(arr)
    arr.array[arr.len] = new_elt
    arr.len += 1
    return arr

# extend an ArrayLen's length if necessary
def maybe_extend_array(arr):
    if (len(arr.array) == arr.len):
        new_array = ([None] * (round(arr.len * size_incr_factor)))
        for i in range(0, arr.len):
            new_array[i] = arr.array[i]
        arr.array = new_array
    return None

# insert an element at a particular index in an array
def add(arr,index,new_elt):
    if ((index > arr.len) or (index < 0)):
        raise IndexError
    maybe_extend_array(arr)
    arr.len += 1
    for x in range(arr.len,index,-1):
        arr.array[x] = arr.array[x-1]
    arr.array[index] = new_elt
    return arr

# get the element at the specified index in an array
def get(arr,index):
    if ((index >= arr.len) or (index < 0)):
        raise IndexError
    return arr.array[index]

def set(arr,index,new_elt):
    if ((index >= arr.len) or (index < 0)):
        raise IndexError
    arr.array[index]=new_elt
    return arr

def remove(arr,index):
    if ((index >= arr.len) or (index < 0)):
        raise IndexError
    arr.len -= 1
    # nb: must now be at least one extra element
    for x in range(index,arr.len):
        arr.array[x] = arr.array[x+1]
    # not necessary, but tidier:
    arr.array[arr.len] = None
    return arr