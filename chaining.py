from __future__ import annotations
import hashlib


class Node:
    def __init__(self, key, value, next_node):
        self.key = key
        self.value = value
        self.next_node = next_node


class ChainedHash:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * self.capacity
        self.p = None
        self.pp = None

    def hash_value(self, key):
        if isinstance(key, int):
            return key % self.capacity
        return int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity

    def search(self, key):

        hash_index = self.hash_value(key)
        self.p = self.table[hash_index]
        self.pp = None
        while self.p:
            if self.p.key == key:
                return self.p.value
            self.pp = self.p
            self.p = self.p.next_node

        return None

    def add(self, key, value):
        hash_index = self.hash_value(key)
        p = self.table[hash_index]
        while p:
            if p.key == key:
                return False
            p = p.next_node

        temp = Node(key, value, self.table[hash_index])
        self.table[hash_index] = temp
        return True

    def remove(self, key):
        target = self.search(key)
        if target:
            if self.pp:
                self.pp = self.p.next_node
            else:
                self.table[self.hash_value(key)] = self.p.next_node
            return True
        return False

    def dump(self):
        for i in range(self.capacity):
            self.p = self.table[i]
            print(i, end=' ')
            while self.p:
                print(f'  ->{self.p.key} ({self.p.value})', end=' ')
                self.p = self.p.next_node
            print()


table = ChainedHash(13)
while True:
    s = int(input())
    if s == 0:
        break
    else:
        table.add(s, s)

table.dump()