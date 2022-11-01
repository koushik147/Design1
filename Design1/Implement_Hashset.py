#TimeComplexity: O(1)
#SpaceComplexity: O(n)
class MyHashSet(object):

    def __init__(self):
        self.length = 1000 # creating length variable and providing input
        self.primary = [None]*self.length # declaring primary as empty for size length

    def hashkey(self,key):
        return key%self.length # finding the first hashkey
    
    def doublehashkey(self,key):
        return key//self.length # finding the second hashkey
    
    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        hash_index=self.hashkey(key) # storing the first hashkey
        double_hash_index=self.doublehashkey(key) # storing the second hashkey
        if self.primary[hash_index] == None: # if primary array is empty
            if hash_index == 0: # if creating secondary array in index 0
                self.primary[hash_index] = [False] * (self.length + 1) # creating secondary array with value false for length + 1
            else: # if creating secondary array in index other than 0
                self.primary[hash_index] = [False] * (self.length) # creating secondary array with value false for length
        self.primary[hash_index][double_hash_index] = True # Assigning value as true for the specified index

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hash_index=self.hashkey(key) # storing the first hashkey
        double_hash_index=self.doublehashkey(key) # storing the second hashkey
        if self.primary[hash_index] !=None: # if primary array value is none
            self.primary[hash_index][double_hash_index] = False # Assigning value as false for the specified index

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        hash_index=self.hashkey(key) # storing the first hashkey
        double_hash_index=self.doublehashkey(key) # storing the seconf hashkey
        if self.primary[hash_index] !=None: # if primary array value is none
            return self.primary[hash_index][double_hash_index] # returning specified value from primary array
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
