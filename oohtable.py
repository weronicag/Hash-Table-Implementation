class HashTable:
    def __init__(self, nbuckets=0):
        self.table = [[] for _ in range(nbuckets)]
        self.table_len = len(self.table)
        self.key_list = []
        self.iterations = iter(self.key_list)

    def __len__(self):
        "Counts the elements within the hash table"
        return sum([len(bucket) for bucket in self.table])

    def bucket_indexof(self, key):
        "Return the index of the element within a specific bucket"
        bucket_lst = self.table[hash(key) % self.table_len]
        for idx in range(len(bucket_lst)):
            if bucket_lst[idx][0] == key:
                return idx
        return None

    def __setitem__(self, key, value):
        """Perform the equivalent of table[key] = value
        Finds the appropriate bucket indicated by key and then appends (key,value)"""
        #storing the keys for faster look up later
        self.key_list.append(key)
        hash_idx = hash(key) % self.table_len
        bucket_lst = self.table[hash_idx]
        #get the index of the key within the bucket
        tuple_idx = self.bucket_indexof(key)
        if tuple_idx is None:
            bucket_lst.append((key, value))
        else:
            bucket_lst[tuple_idx] = (key, value)

    def __getitem__(self, key):
        """Return the equivalent of table[key]
        Find the appropriate bucket indicated by the key and look for the
        association with the key."""
        hash_idx = hash(key) % self.table_len
        bucket_lst = self.table[hash_idx]
        key_of_bucket = self.bucket_indexof(key)
        if key_of_bucket is not None:
            return bucket_lst[key_of_bucket][1]
        return None

    def __contains__(self, key):
        "Test for membership"
        if key in self.key_list:
            return True
        return False

    def __iter__(self):
        "Returns an iteration over the keys in the hashtable"
        return self.iterations

    def keys(self):
        return sorted(self.key_list)

    def items(self):
        "Gets a list of keyvalue pairs in the format ('the', 9)"
        item_list = []
        for i in range(self.table_len):
            for j, d in enumerate(self.table[i]):
                item_list.append((d[0],d[1],))
        return item_list

    def __repr__(self):
        return self.table.__str__()

    def __str__(self):
        item_list = []
        for i in range(self.table_len):
            for j, d in enumerate(self.table[i]):
                item_list.append(f"{d[0]}:{d[1]}")
        return '{' + ", ".join(item_list) + '}'
