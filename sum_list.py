"""sum_list.py"""
from timeit import timeit
from typing import Optional


class Node:  # pylint: disable=too-few-public-methods
    """Node class for linked list structure."""

    def __init__(self, val: Optional[int]) -> None:
        self.val = val
        self.next: Optional[Node] = None


def linked_list_sum_iterative(head: Optional[Node]) -> Optional[int]:
    """Iterate through linked list and return sum of all Node values."""
    value: Optional[int] = None
    if not head:
        return value
    value = 0
    current: Optional[Node] = head
    while current:
        if current.val:
            value += current.val
        current = current.next
    return value


def linked_list_sum_recursive(head: Optional[Node]) -> Optional[int]:
    """Recursively traverse through linked list and return sum of all
    Node values."""
    value: Optional[int] = None
    if not head:
        return value
    value = 0
    if head.val:
        value = head.val
    next_value = linked_list_sum_recursive(head.next)
    if next_value:
        value += next_value
    return value


# LINKED LIST
# A -> B -> C -> D -> None
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d

# TESTS
assert linked_list_sum_iterative(a) == 10
assert linked_list_sum_iterative(b) == 9
assert linked_list_sum_iterative(d) == 4
assert not linked_list_sum_iterative(None)

assert linked_list_sum_recursive(a) == 10
assert linked_list_sum_recursive(b) == 9
assert linked_list_sum_recursive(d) == 4
assert not linked_list_sum_recursive(None)

# TIME TESTS
print("\nlinked_list_sum_iterative:")
print(timeit(lambda: linked_list_sum_iterative(a), number=1000000))
print("\nlinked_list_sum_recursive:")
print(timeit(lambda: linked_list_sum_recursive(a), number=1000000))
