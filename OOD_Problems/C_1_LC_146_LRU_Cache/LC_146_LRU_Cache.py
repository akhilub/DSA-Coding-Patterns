#Approach1: Ordered Dictionary

'''
example:

>>> od = collections.OrderedDict()
>>>
>>> od[1]=1
>>> od[2]=2
>>> od[3]=3
>>>
>>> od
OrderedDict([(1, 1), (2, 2), (3, 3)])
>>> od.move_to_end(1)
>>> od
OrderedDict([(2, 2), (3, 3), (1, 1)])
>>>
>>> od.get(1)
1
>>> od.popitem()
(1, 1)
>>> od
OrderedDict([(2, 2), (3, 3)])
>>>
>>> od[1]=1
>>> od
OrderedDict([(2, 2), (3, 3), (1, 1)])
>>>
>>> od.popitem(last=False)
(2, 2)
>>> od
OrderedDict([(3, 3), (1, 1)])

'''

from collections import *

class LRUCache:
    def __init__(self, capacity: 'int'):
        self.cache = OrderedDict()
        self.remain = capacity

    def get(self, key: 'int') -> 'int':
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key) # meaning end is the most recently used
        return self.cache.get(key)

    def put(self, key: 'int', value: 'int') -> 'None':
        if key not in self.cache:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.cache.popitem(last=False) # pop start position
        else:
            self.cache.pop(key)
        self.cache[key] = value # add to end of dict, meaning most recently used
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


#Approach2: Dictionary + Doubly Linked List
'''
My Thoughts
- Use a dictionary to store cache entries for O(1) access.
- Use a doubly linked list to maintain the order of usage, with head being the most recently used and tail being the least recently used.
- Define helper methods to remove a node from the list and to add a node to the head of the list.
- In the get method, if the key exists, move the corresponding node to the head of the list and return its value.
- In the put method, if the key exists, remove the old node. Add the new node to the head of the list. If the cache exceeds capacity, remove the node from the tail of the list.

'''

class Node:
    def __init__(self,key = None, value = None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self,node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_head(self,node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_head(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key,value)
        self._add_to_head(node)
        self.cache[key] = node
        if len(self.cache)>self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Complexity
'''
- Time: O(1) for both get and put operations, as dictionary operations and linked list operations are O(1).
- Space: O(capacity) for storing the cache entries.
'''