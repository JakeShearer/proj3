import math
import huffman

class Song:
    def __init__(self, songinfo):
        self.fullstring = songinfo
        splitinfo = songinfo.split("--")
        self.number = None
        self.title = splitinfo[0]
        self.artist = splitinfo[1]
        self.album = splitinfo[2]

# AnyList is one of
# None
# Pair(value, rest)
class Pair:
    def __init__(self, value, rest):
        self.value = value  # any value
        self.rest = rest  # an AnyList

    def __eq__(self, other):
        return type(other) == Pair and self.value == other.value and \
               self.rest == other.rest

    def __repr__(self):
        return ("%r, %r" % (self.value, self.rest))


# None
# returns an empty AnyList
def make_empty():
    return None


# AnyList int value => AnyList
# adds a value to an AnyList at a certain index

def add(list, index, value):
    if index < 0:
        raise IndexError
    else:
        if list == None and index == 0:
            return Pair(value, None)
        elif list == None and index > 0:
            raise IndexError
        if index == 0:
            return Pair(value, Pair(list.value, list.rest))
        else:
            return Pair(list.value, add(list.rest, index - 1, value))


# AnyList => int
# determines tliste number of elements in a list
def length(list):
    if list == None:
        return 0
    else:
        return 1 + length(list.rest)


# AnyList int => value
# returns tliste value at a given index
def get(list, index):
    if index < 0:
        raise IndexError
    else:
        if list == None and index >= 0:
            raise IndexError
        elif index == 0:
            return list.value
        else:
            return get(list.rest, index - 1)


# AnyList int value => AnyList
# replaces tliste value at a specified index witlist a given value
def set(list, index, value):
    if index < 0:
        raise IndexError
    else:
        if list == None and index >= 0:
            raise IndexError
        elif index == 0:
            return Pair(value, list.rest)
        else:
            return Pair(list.value, set(list.rest, index - 1, value))


# AnyList int => AnyList
# removes an item from an AnyList at a given index and returns tlistat list
def remove_help(list, index):
    if index < 0:
        raise IndexError
    else:
        if list == None and index >= 0:
            raise IndexError
        elif index == 0:
            return list.rest
        else:
            return Pair(list.value, remove_help(list.rest, index - 1))


# AnyList int => Tuple
# removes a specified item from a list and returns tlistat item and tliste remaining list
def remove(list, index):
    rem_value = get(list, index)
    rem_list = remove_help(list, index)
    return rem_value, rem_list


# AnyList function => None
# applies a function to each element in a list
def foreach(list, function):
    if list == None:
        return None
    else:
        function(list.value)
        foreach(list.rest, function)


# sort Anylist => AnyList
# sorts a linked list using insertion sort and returns the sorted list
def sort(library, less_than):
    # print ("sorting by " + str(key))
    print("LESS_THAN" + str(less_than))
    if library == None:
        return None
    sortedList = library
    library = library.rest
    sortedList.rest = None
    cnt = 0
    while cnt < length(library):
        curr = library
        library = library.rest
        #print(type(curr.value))
        #print(type(sortedList.value))
        #print(type(less_than))
        if less_than(curr.value, sortedList.value) == -1:  # getattr(sortedList.value, key) > getattr(curr.value, key):
            curr.rest = sortedList
            sortedList = curr
        else:
            # Searclist list for correct position of current.
            search = sortedList
            while search.rest != None and less_than(curr.value,
                                                    search.rest.value) == 1:  # curr.value > search.rest.value:
                search = search.rest
            # current goes after searclist.
            curr.rest = search.rest
            search.rest = curr
    cnt += 1
    return sortedList

#sort_helper() AnyList-->AnyList
#helper method for the sort function
def sort_helper(library, key):
    # create a list of split songs from the library
    split_list = make_empty()
    cnt = 0
    # sort(library, key)
    # if the list has been sorted already
    # while cnt < length(library):
    #   if isinstance(get(library, cnt), str) == False:
    #      return sort(library, key)
    # if the list has not yet been converted to Song class
    # library = foreach(library, converttoSong)

    if key == "0":
        return sort(library, less_than_number)
    elif key == "1":
        return sort(library, less_than_title)
    elif key == "2":
        return sort(library, less_than_artist)
    elif key == "3":
        return sort(library, less_than_album)
    else:
        print("key error")
        return

#less_than_number() Song1, Song2 --> int
# Compares two songs
def less_than_number(song1, song2):
    if song1.number < song2.number:
        return -1
    if song1.number > song2.number:
        return 1
    if song1.number == song2.number:
        return 0

#less_than_title() Song1, Song2 --> int
# Compares two songs
def less_than_title(song1, song2):
    if song1.title < song2.title:
        return -1
    if song1.title > song2.title:
        return 1
    if song1.title == song2.title:
        return 0

#less_than_album() Song1, Song2 --> int
# Compares two songs
def less_than_album(song1, song2):
    if song1.album < song2.album:
        return -1
    if song1.album > song2.album:
        return 1
    if song1.album == song2.album:
        return 0

#less_than_artist() Song1, Song2 --> int
# Compares two songs
def less_than_artist(song1, song2):
    if song1.artist < song2.artist:
        return -1
    if song1.artist > song2.artist:
        return 1
    if song1.artist == song2.artist:
        return 0

#insert_sorted list, val, func >> list
#inserts a value into a sorted list        
def insert_sorted(list, val, comes_before):
   #print ("inserting " + str(val) + " in list")
   if list == None:
      list = Pair(val, None)
      #print ("added val to front of list")
      return list
   if comes_before(val, list.value):
      return Pair(val, list)
   else:
      return Pair(list.value, insert_sorted(list.rest, val, comes_before))
   '''
   idx = 0
   #print ("list length: " + str(length(list)))
   while idx < length(list):
      if list == None:
         list = add(list, idx, val)
      #print("grabbing val at index " + str(idx))
      #print ("adding if " + str(get(list, idx)) + " is greater than " + str(val))
      if comes_before(val, get(list, idx)):
         #print (idx)
         list = add(list, idx, val)
         return list
      if list.rest == None:
         list = add(list, length(list), val)
         return list
      else:
         #print ("incrementing idx")
         idx += 1
   #print ("never added value to list")
   list = add(list, length(list), val)
   '''
   return list
   
#reverse list --> list
#reverses a linked list and returns it      
def reverse(linkedlist):
   prev = None
   current = linkedlist
   while(current is not None):
      next = current.rest
      current.rest = prev
      prev = current
      current = next
   linkedlist = prev
   return linkedlist