class HashTableWithoutReplacement:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        start_index = index

        # Search for an empty slot moving linearly
        while self.table[index] is not None:
            if self.table[index] == key:
                print(f"Key {key} already exists at index {index}.")
                return
            index = (index + 1) % self.size
            if index == start_index:
                print(f"Hash table is full! Could not insert {key}.")
                return

        self.table[index] = key
        print(f"Inserted {key} at index {index}.")

    def search(self, key):
        index = self.hash_function(key)
        start_index = index

        while self.table[index] is not None:
            if self.table[index] == key:
                return index
            index = (index + 1) % self.size
            if index == start_index:
                break
        return -1

    def display(self):
        print("\nHash Table (Without Replacement):")
        for i, val in enumerate(self.table):
            print(f"  Index {i}: {val}")


# --- Example Usage ---
ht = HashTableWithoutReplacement(7)
for k in [24, 17, 31, 10, 45]:
    ht.insert(k)

ht.display()
print("\nSearch 31 -> Index:", ht.search(31))
print("Search 99 -> Index:", ht.search(99))