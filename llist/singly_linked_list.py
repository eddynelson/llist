from typing import Optional
from typing import Dict

from llist.node import SinglyNode

class SinglyLinkedList():
    def __init__(self) -> None:
        self.size: int = 0
        self._head: Optional[SinglyNode] = None
        self._tail: Optional[SinglyNode] = None
    
    @property
    def head(self) -> SinglyNode:
        return self._head
    
    @head.setter
    def head(self, node: SinglyNode) -> None: 
        if self.size == 0:
            self._head = node
        else:
            _node = self.head
            
            while True:
                if _node.next == None:
                    _node.next = node
                    self._tail = node
                    break
                
                _node = _node.next
        
        self.size += 1
    
    @property
    def tail(self) -> SinglyNode:
        return self._tail
    
    # def map(self, fn: Callable) -> None:
    #     node = self._head
        
    #     while node is not None:
    #         node.value = fn(node.value)
    #         node = node.next