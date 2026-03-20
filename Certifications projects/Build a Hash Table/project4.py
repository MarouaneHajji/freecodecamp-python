class HashTable:
    """
    A simple Hash Table implementation using Python dictionaries.

    Internally, the table uses a nested dictionary structure:
        { hash_value: { original_key: value, ... }, ... }

    When two different keys produce the same hash (a "collision"),
    they are stored together under the same hash_value bucket.
    """

    def __init__(self):
        # The main storage for all key-value pairs.
        # Keys are hash values (integers), values are nested dicts.
        self.collection = {}

    def hash(self, key):
        """
        Converts a string key into a numeric hash value.

        Example: hash('golf') -> ord('g') + ord('o') + ord('l') + ord('f')
                              -> 103 + 111 + 108 + 102 = 424
        """
        return sum(ord(char) for char in key)

    def add(self, key, value):
        """
        Adds a key-value pair to the hash table.

        If the hash bucket already exists (collision), the new pair is
        inserted into the existing nested dictionary. Otherwise a new
        bucket is created.
        """
        hashed = self.hash(key)

        if hashed in self.collection:
            # Bucket already exists — add the new pair into it (handles collisions)
            self.collection[hashed][key] = value
        else:
            # No bucket yet — create a new one with this key-value pair
            self.collection[hashed] = {key: value}

    def remove(self, key):
        """
        Removes a specific key-value pair from the hash table.

        Only deletes the exact key — other keys in the same bucket are
        untouched. Does nothing if the key doesn't exist.
        """
        hashed = self.hash(key)

        # Only attempt deletion if both the bucket and the exact key exist
        if hashed in self.collection and key in self.collection[hashed]:
            del self.collection[hashed][key]

    def lookup(self, key):
        """
        Retrieves the value associated with a given key.

        Returns the value if found, or None if the key doesn't exist.
        """
        hashed = self.hash(key)

        # Verify the bucket exists and contains the exact key before returning
        if hashed in self.collection and key in self.collection[hashed]:
            return self.collection[hashed][key]

        return None