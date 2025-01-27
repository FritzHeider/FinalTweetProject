
from linkedlist import *

class Queue:
    def __init__(self, items=None):
        self.list = LinkedList(items)
        self.len = 0

    def __str__(self):
        return " ".join(self)

    def __iter__(self):
        return self.list.__iter__()

    def length(self):
        return self.len


    def enqueue(self, item):
        self.list.append(item)
        self.len += 1

    def dequeue(self):
        item = self.list.head
        if self.length() > 0:
            self.list.delete(item.data)
            self.len -= 1
            return item.data
        else:
            print("No")_str__(self):
        return " ".join(self)

    def __iter__(self):
        return self.list.__iter__()

    def length(self):
        return self.len


    def enqueue(self, item):
        self.list.append(item)
        self.len += 1

    def dequeue(self):
        item = self.list.head
        if self.length() > 0:
            self.list.delete(item.data)
            self.len -= 1
            return item.data
        else:
            print("No")
