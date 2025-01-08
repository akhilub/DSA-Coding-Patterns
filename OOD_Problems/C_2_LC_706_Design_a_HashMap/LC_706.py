#Approach:Chaining 
'''
A straightforward approach to implement a hash map is to use chaining with a list of buckets, 
where each bucket is a list (or linked list) of tuples representing key-value pairs.

- Since all keys and values are in the range of [0, 1000000], create an array with length 1000001, which has int type. 
Initially, all the elements in the array are -1.

- For the put function, set the value at index key in the array to be value.

- For the remove function, set the value at index key in the array to be -1.

- For the get function, simply return the element at index key.

- Some of the questions which can be asked to the interviewer before implementing the solution:

• For simplicity, are the keys integers only?
• For collision resolution, can we use chaining?
• Do we have to worry about load factors?
• Can we assume inputs are valid or do we have to validate them?
• Can we assume this fits memory?
'''

class MyHashMap:

    def __init__(self):
        self.d = [-1]*1000001
        

    def put(self, key: int, value: int) -> None:
        self.d[key]=value
        

    def get(self, key: int) -> int:
        return self.d[key]
        

    def remove(self, key: int) -> None:
        return self.d[key]=-1




#Write this in interviews
#Approach:Using a Hash Function
'''
We need a hash function that allows to distribute keys “evenly” to the fixed-size hash table (less collision). 
If there is a collision, i.e. h(a)=h(b) if a is not equal to b, we need to append them to a list.

To get the value of a key, we first compute the hash key, then go through the list to find if the original key exists.

To update the value of a key, similarly, we need to locate the entry if it exists, update it. Otherwise, the pair (key, value) should be appended to the list (or linked list).

To remove a key-value pair, we locate it if it exists and remove it by copying over the last element of the list, and shrink it by pop().

If the hash function is practically fast enough and does not incur much collision, the complexity of Get, Update and Remove for a hash table is O(1) constant.
'''

class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 65537                                # better to be a prime number, less collision
        self.d = [[] for _ in range(self.size)]          # store (key, value) in the bucket                     # d - data or buckets
    
    def hash(self,key):
        """
        Generate a hash for a given key.
        """
        return key % self.size 

    def put(self, key: int, value: int) -> None:
        """
        Value will always be non-negative.
        """
        hash_key = self.hash(key)
        for i in range(len(self.d[hash_key])):             #use n = len(self.d[hash_key])
            if self.d[hash_key][i][0]==key:
                self.d[hash_key][i] = [key,value]
                return
        self.d[hash_key].append([key,value])
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
        """
        hash_key = self.hash(key)
        for i in range(len(self.d[hash_key])):
            if self.d[hash_key][i][0] ==key:
                return self.d[hash_key][i][1]
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key.
        """
        hash_key = self.hash(key)
        for i in range(len(self.d[hash_key])):
            if self.d[hash_key][i][0]==key:
                del self.d[hash_key][i]
                return 
        


#Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
#obj.put(key,value)
#obj.get(key)
#obj.remove(key)
obj.put(1, 1); # The map is now [[1,1]]
obj.put(2, 2); # The map is now [[1,1], [2,2]]
obj.get(1);    # return 1, The map is now [[1,1], [2,2]]
obj.get(3);    # return -1 (i.e., not found), The map is now [[1,1], [2,2]]
obj.put(2, 1); # The map is now [[1,1], [2,1]] (i.e., update the existing value)
obj.get(2);    # return 1, The map is now [[1,1], [2,1]]
obj.remove(2); # remove the mapping for 2, The map is now [[1,1]]
obj.get(2);    # return -1 (i.e., not found), The map is now [[1,1]]

print(obj.d)