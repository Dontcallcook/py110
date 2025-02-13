"""
PROBLEM:
create a circular buffer class. the class should behave like so:
- when an object is added to the buffer
    if there is space:
        it is added following the most recently added object
    if the buffer is already full:
        replace the oldest object in buffer

- .get() should remove and return oldest object, None if buffer empty

        
EXAMPLE:
** .put(1), .put(1), .put(2), .get(), put(1)
** buffer = [None, None, None]   ----->    insertion_order = []
** buffer = [1, None, None]      ----->    insertion_order = [0]
** buffer = [1, 1, None]         ----->    insertion_order = [0, 1]
** buffer = [1, 1, 2]            ----->    insertion_order = [0, 1, 2]
** buffer = [None, 1, 2]         ----->    insertion_order = [1, 2]
** buffer = [1, 1, 2]            ----->    insertion_order = [1, 2, 0]


ALGORITHM:

high-level strategy:
I will add objects to replace None in buffer by checking the last indx in insertion_order, and placing the object in buffer at (this index + 1) % length of buffer.
I will store the insertion index in insertion_order. 
If an object needs to be removed, i will check the first value of insertion_order to find the index of the oldest object.
I will remove this index from insertion_order, return the oldest object from buffer, and replace the oldest object in buffer to None.


set a buffer as a list of None objects
** buffer = [None, None, None]

set an empty list, _insertion_order, to store the objects' orders of insertion
** insertion_order = []

>> .put()
check if all values in buffer == None
    if they do:
        replace first None with value
        add 0 to insertion_order
elif all values in buffer != None:    
    check first index of insertion order
    change the object located in buffer at this index to new argument object
    update insertion order with new index
else:
    check last index in insertion_order
    insert obect into buffer at this (index + 1) % lenght of buffer
    update last added object's index to insertion_order

>> .get()
check if all values in buffer == None
    if they do:
        return None
    else:
        check first index of insertion order
        return the object located at this index from buffer
        change this object to None in buffer
        pop index from insertion_order

** buffer = [4, 5, 3]
** insertion_order = [2, 0, 1]


"""

class CircularBuffer:
    def __init__(self, buffer_size):
        self._buffer_size = buffer_size
        self._buffer = []
    
    def put(self, obj):
        if all(item == None for item in self._buffer):
            self._buffer[0] = obj
            self._insertion_order.append(0)
        elif all(item != None for item in self._buffer):
            self._buffer[self._insertion_order[0]] = obj
            self._insertion_order.append(self._insertion_order[0])
        else:
            insertion_index = (self._insertion_order[-1] + 1) % self._buffer_size
            self._buffer[insertion_index] = obj
            self._insertion_order.append(insertion_index)
    
    def get(self):
        if all(item == None for item in self._buffer):
            return None
        else:
            get_index = self._insertion_order.pop(0)
            get_value = self._buffer[get_index]
            self._buffer[get_index] = None
            return get_value
    
# [2, None]
buffer = CircularBuffer(3)

print(buffer.get() is None)          # True

buffer.put(1)
buffer.put(2)
print(buffer.get() == 1)             # True

buffer.put(3)
buffer.put(4)
print(buffer.get() == 2)             # True

buffer.put(5)
buffer.put(6)
buffer.put(7)
print(buffer.get() == 5)             # True
print(buffer.get() == 6)             # True
print(buffer.get() == 7)             # True
print(buffer.get() is None)          # True

buffer2 = CircularBuffer(4)

print(buffer2.get() is None)         # True

buffer2.put(1)
buffer2.put(2)
print(buffer2.get() == 1)            # True

buffer2.put(3)
buffer2.put(4)
print(buffer2.get() == 2)            # True

buffer2.put(5)
buffer2.put(6)
buffer2.put(7)
print(buffer2.get() == 4)            # True
print(buffer2.get() == 5)            # True
print(buffer2.get() == 6)            # True
print(buffer2.get() == 7)            # True
print(buffer2.get() is None)         # True