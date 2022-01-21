"""linked_list_find.py"""
from timeit import timeit
from typing import Optional


class Node:  # pylint: disable=too-few-public-methods
    """Node class for linked list structure."""

    def __init__(self, val: Optional[str]) -> None:
        self.val = val
        self.next: Optional[Node] = None


def linked_list_find_iterative(head: Optional[Node],
                               target: Optional[str]) -> bool:
    """Iterate through linked list and return True if target
    is found, False otherwise."""
    current: Optional[Node] = head
    while current:
        if current.val == target:
            return True
        current = current.next
    return False


def linked_list_find_recursive(head: Optional[Node],
                               target: Optional[str]) -> bool:
    """Recursively traverse through linked list and return True
    is target is found, False otherwise."""
    if not head:
        return False
    if head.val == target:
        return True
    return linked_list_find_recursive(head.next, target)


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
assert linked_list_find_iterative(a, "B")
assert linked_list_find_iterative(a, "D")
assert linked_list_find_iterative(b, "C")
assert not linked_list_find_iterative(a, "F")
assert not linked_list_find_iterative(None, "A")
assert not linked_list_find_iterative(a, None)
assert not linked_list_find_iterative(None, None)

assert linked_list_find_recursive(a, "B")
assert linked_list_find_recursive(a, "D")
assert linked_list_find_recursive(b, "C")
assert not linked_list_find_recursive(a, "F")
assert not linked_list_find_recursive(None, "A")
assert not linked_list_find_recursive(a, None)
assert not linked_list_find_recursive(None, None)

# TIME TESTS
print("\nlinked_list_find_iterative:")
print(timeit(lambda: linked_list_find_iterative(a, "D"), number=1000000))
print("\nlinked_list_find_recursive:")
print(timeit(lambda: linked_list_find_recursive(a, "D"), number=1000000))
