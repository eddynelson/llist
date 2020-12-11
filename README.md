# lllist

This is a implementation of the data structure algorithms Single linked list and Doubly linked list in python 3.8+

# Usage

## For single linked list

``` python

from llist import SinglyLinkedList
from llist.node import SinglyNode

# Create a singly linked list
my_llist = SinglyLinkedList()

# Add element, equivalent to append in a list
my_llist.head = SinglyNode(3)

# Get last element with tail
print(my_llist.tail.value)

# Add an element at the first
my_llist.addFirst(SinglyNode('a'))

# Get first element
print(my_llist.head)

```

## For doubly linked list

Coming soon