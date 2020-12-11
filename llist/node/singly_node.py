from typing import Any
from typing import Union

class SinglyNode():
    def __init__(
        self, 
        value: Any, 
        next: Union[int, None] = None) -> None:
        
        self.value = value
        self.next = next