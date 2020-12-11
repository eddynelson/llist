from typing import Any
from typing import Union

class DoublyNode():
    def __init__(
        self, value: Any,
        prev: Union[int, None],
        next: Union[int, None]) -> None:
        
        self.value = value
        self.next = next
        self.prev = prev