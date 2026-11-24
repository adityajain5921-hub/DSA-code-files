class HashTableWithReplacement:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def _find_next_empty(self, start_index):
        index = start_index
        while self.table[index] is not None:
            index = (index + 1) % self.size
            if index == start_index:
                return -1  # Table is full
        return index

    def insert(self, key):
        home_index = self.hash_function(key)

        # Case 1: Home slot is empty -> place directly
        if self.table[home_index] is None:
            self.table[home_index] = key
            print(f"Inserted {key} at its home index {home_index}.")
            return

        if self.table[home_index] == key:
            print(f"Key {key} already exists at index {home_index}.")
            return

        # Check if table is full before attempting replacement
        empty_index = self._find_next_empty(home_index)
        if empty_index == -1:
            print(f"Hash table is full! Could not insert {key}.")
            return

        occupant = self.table[home_index]
        occupant_home = self.hash_function(occupant)

        # Case 2: Occupant is NOT at its own home index -> replace it!
        if occupant_home != home_index:
            self.table[home_index] = key
            self.table[empty_index] = occupant
            print(
                f"Inserted {key} at home index {home_index}, "
                f"moving displaced {occupant} to index {empty_index}."
            )
        # Case 3: Occupant IS at its own home index -> keep occupant, probe for new key
        else:
            self.table[empty_index] = key
            print(
                f"Index {home_index} belongs to {occupant}; "
                f"placed {key} at next empty index {empty_index}."
            )

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
        print("\nHash Table (With Replacement):")
        for i, val in enumerate(self.table):
            print(f"  Index {i}: {val}")


# --- Example Usage ---
ht_rep = HashTableWithReplacement(7)
for k in [27, 13, 20, 34]:
    ht_rep.insert(k)

ht_rep.display()
print("\nSearch 20 -> Index:", ht_rep.search(20))