class MyHashSet:

    def __init__(self):
        self.hashtable=set()

    def add(self, key: int) -> None:
        self.hashtable.add(key)

    def remove(self, key: int) -> None:
        if key in self.hashtable:
            self.hashtable.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.hashtable:return True

