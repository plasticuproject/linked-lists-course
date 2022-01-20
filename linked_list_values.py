"""linked_list_values.py"""
from timeit import timeit
from typing import Optional, List


class Node:  # pylint: disable=too-few-public-methods
    """Node class for linked list structure."""

    def __init__(self, val: Optional[str]) -> None:
        self.val = val
        self.next: Optional[Node] = None


def linked_list_values_iterative(head: Optional[Node]) -> List[str]:
    """Iterate through linked list and return array of all Node values."""
    current: Optional[Node] = head
    values: List[str] = []
    while current:
        if current.val:
            values.append(current.val)
        current = current.next
    return values


def linked_list_values_recursive(head: Optional[Node]) -> List[str]:
    """Recursively traverse through linked list and return array of all
    Node values."""
    values: List[str] = []
    if not head:
        return values
    if head.val:
        values.append(head.val)
    values += linked_list_values_recursive(head.next)
    return values


def alt_linked_list_values_recursive(head: Optional[Node]) -> List[str]:
    """Alternate function to travers through a linked list and return
    array of all Node values, using the _fill_values() helper funtion
    to perform recursion and update the values array."""
    values: List[str] = []
    _fill_values(head, values)
    return values


def _fill_values(head: Optional[Node], values: List[str]) -> None:
    """Helper function for alt_linked_list_values_recursive().
    Recursively appends Node values to argument array."""
    if not head:
        return
    if head.val:
        values.append(head.val)
    _fill_values(head.next, values)


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
assert linked_list_values_iterative(a) == ["A", "B", "C", "D"]
assert linked_list_values_iterative(d) == ["D"]
assert not linked_list_values_iterative(None)

assert linked_list_values_recursive(a) == ["A", "B", "C", "D"]
assert linked_list_values_recursive(d) == ["D"]
assert not linked_list_values_recursive(None)

assert alt_linked_list_values_recursive(a) == ["A", "B", "C", "D"]
assert alt_linked_list_values_recursive(d) == ["D"]
assert not alt_linked_list_values_recursive(None)

# TIME TESTS
print("\nlinked_list_values_iterative:")
print(timeit(lambda: linked_list_values_iterative(a), number=1000000))
print("\nlinked_list_values_recursive:")
print(timeit(lambda: linked_list_values_recursive(a), number=1000000))
print("\nalt_linked_list_values_recursive:")
print(timeit(lambda: alt_linked_list_values_recursive(a), number=1000000))
