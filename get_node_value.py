"""get_node_value.py"""
from timeit import timeit
from typing import Optional


class Node:  # pylint: disable=too-few-public-methods
    """Node class for linked list structure."""

    def __init__(self, val: Optional[str]) -> None:
        self.val = val
        self.next: Optional[Node] = None


def get_node_value_iterative(head: Optional[Node],
                             idx: Optional[int]) -> Optional[str]:
    """Iterate through linked list and return Node value at
    provided index location."""
    if not idx:
        idx = 0
    idx_count: int = 0
    current: Optional[Node] = head
    while current:
        if idx_count == idx:
            return current.val
        current = current.next
        idx_count += 1
    return None


def get_node_value_recursive(head: Optional[Node],
                             idx: Optional[int]) -> Optional[str]:
    """Recursively traverse through linked list and return Node
    value at provided index location."""
    if not head:
        return None
    if not idx:
        idx = 0
    if idx == 0:
        return head.val
    return get_node_value_recursive(head.next, idx - 1)


# LINKED LIST
# A -> B -> C -> D -> None
a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

a.next = b
b.next = c
c.next = d

# TESTS
assert get_node_value_iterative(a, 0) == "A"
assert get_node_value_iterative(a, 2) == "C"
assert get_node_value_iterative(b, 0) == "B"
assert get_node_value_iterative(c, 1) == "D"
assert get_node_value_iterative(a, None) == "A"
assert not get_node_value_iterative(None, 0)
assert not get_node_value_iterative(None, None)
assert not get_node_value_iterative(a, 10)

assert get_node_value_recursive(a, 0) == "A"
assert get_node_value_recursive(a, 2) == "C"
assert get_node_value_recursive(b, 0) == "B"
assert get_node_value_recursive(c, 1) == "D"
assert get_node_value_recursive(a, None) == "A"
assert not get_node_value_recursive(None, 0)
assert not get_node_value_recursive(None, None)
assert not get_node_value_recursive(a, 10)

# TIME TESTS
print("\nget_node_value_iterative:")
print(timeit(lambda: get_node_value_iterative(a, 0), number=1000000))
print("\nget_node_value_recursive:")
print(timeit(lambda: get_node_value_recursive(a, 0), number=1000000))
