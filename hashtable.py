class HashTable(object):
    def __init__(self, size):
        if not(type(size) == int):
            raise TypeError("Input an int for size")
        elif size < 1:
            raise ValueError("Size must be greater than 1")
        self.size = size
        self.itemCount = 0
        number_of_buckets = 1
        while number_of_buckets < size:
            number_of_buckets = number_of_buckets * 2
        self.buckets = [[] for i in range(number_of_buckets)]

    def validate_string(self, key):
        # if the input is not a string
        if not(type(key) == str):
            raise TypeError("Keyname must be a string")

    def begin_action(self, key):
        self.validate_string(key)
        # Hash the value into the total number of slots
        hashed = key.__hash__() % len(self.buckets)
        # Check the bucket where the key would be if it exists
        bucket = self.buckets[hashed]
        # Check the bucket for that key, if it exists delete it
        key_array = [entry[0] for entry in bucket]
        return hashed, bucket, key_array

    def set(self, key, value):
        hashed, bucket, key_array = self.begin_action(key)
        for i, k in enumerate(key_array):
            if key == k:
                bucket[i] = (key,value)
                return True
        # If the hashtable is full, dont add a new value
        # this must come after we check if the key is in the table
        if self.itemCount == self.size:
            return False
        # If key doesnt have a value, don't update
        bucket.append((key,value))
        # Iterate factor for load calculations
        self.itemCount += 1
        return True

    def get(self, key):
        hashed, bucket, key_array = self.begin_action(key)
        for i, k in enumerate(key_array):
            if key == k:
                return bucket[i][1]
        # If the key doesnt exist return none
        return None

    def delete(self, key):
        hashed, bucket, key_array = self.begin_action(key)
        for i, k in enumerate(key_array):
            if key == k:
                # Remove the key, value pair from the array
                deleted_term = bucket.pop(i)
                # Decrement Item count for load calculation
                self.itemCount -= 1
                return deleted_term[1]
        # If they key doesn't exist return none
        return None

    def load(self):
        return float(self.itemCount) / float(self.size)
