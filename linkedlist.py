#!python

from __future__ import print_function


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any"""
        self.head = None
        self.tail = None
        if iterable:
            for item in iterable:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(self.as_list())

    def as_list(self):
        """Return a list of all items in this linked list"""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            # result.append(current)
            current = current.next
        return result

    def is_empty(self):
        """Return True if this linked list is empty, or False"""
        return self.head is None
    #Best Case Omega(n)
    #Worst Case O(n)
    #Answer: Theta(n)
    def length(self):
        """Return the length of this linked list by traversing its nodes"""
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count
    #Best Case Omega(1)
    #Worst Case O(1)
    #Answer: Theta(1)
    def append(self, item):
        """Insert the given item at the tail of this linked list"""
        if self.head is None:
            self.head = Node(item)
            self.tail = self.head
        elif self.head == self.tail:
            self.tail = Node(item)
            self.head.next = self.tail
        else:
            new_tail = Node(item)
            self.tail.next = new_tail
            self.tail = new_tail

    #Best Case Omega(1)
    #Worst Case O(1)
    #Answer: Theta(1)
    def prepend(self, item):
        """Insert the given item at the head of this linked list"""
        if self.head is None:
            self.head = Node(item)
            self.tail = self.head
        elif self.head == self.tail:
            self.head = Node(item)
            self.head.next = self.tail
        else:
            new_head = Node(item)
            new_head.next = self.head
            self.head = new_head

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError"""
        current = self.head

        #Best Case Omega(1)
        #Worst Case O(1)
        #Answer: Theta(1)
        #if LinkedList is empty
        if current is None:
            raise ValueError('Cannot delete because LinkedList is empty.')

        #Best Case Omega(1)
        #Worst Case O(1)
        #Answer: Theta(1)
        #if LinkedList has 1 item
        if current.data == item:
            if current.next is not None:
                self.head = current.next
            else:
                self.head = None
                self.tail = None
            return

        #Best Case Omega(n)
        #Worst Case O(n)
        #Answer: Theta(n)
        #if LinkedList has more than 1 item
        while current.next is not None:
            if current.next.data == item:
                nextNext = current.next.next
                if nextNext is not None:
                    current.next = nextNext
                else:
                    current.next = None
                    self.tail = current
                return
            current = current.next

        raise ValueError("Item coudn't be deleted")
    #Best Case Omega(n)
    #Worst Case O(n)
    #Answer: Theta(n)
    def find(self, quality):
        """Return an item from this linked list satisfying the given quality"""
        current = self.head
        while current is not None:
            if quality(current.data):
                return current.data
            current = current.next

    #Best Case is Omega(1)
    #Worst Case is O(1)
    #Answer: Theta(1)
    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

def test_linked_list():
    ll = LinkedList()
    print(ll)
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())

    ll.delete('A')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('B')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())

if __name__ == '__main__':
    test_linked_list()
