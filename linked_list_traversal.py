"""linked_list_traversal.py"""
from timeit import timeit
from typing import Optional


class Node:  # pylint: disable=too-few-public-methods
    """Node class for linked list structure."""

    def __init__(self, val: Optional[str]) -> None:
        self.val = val
        self.next: Optional[Node] = None


def print_linked_list_iterative(head: Optional[Node]) -> None:
    """Iterate through linked list and print contents."""
    current: Optional[Node] = head
    while current:
        print(current.val)
        current = current.next


def print_linked_list_recursive(head: Optional[Node]) -> Optional[Node]:
    """Recursively traverse through linked list and print contents."""
    if not head:
        return None
    print(head.val)
    print_linked_list_recursive(head.next)
    return head.next


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
print_linked_list_iterative(a)
print_linked_list_iterative(None)

print_linked_list_recursive(a)
print_linked_list_recursive(None)

# TIME TESTS
PLTIT = timeit(lambda: print_linked_list_iterative(a), number=1000000)
PLIRT = timeit(lambda: print_linked_list_recursive(a), number=1000000)
print("\nprint_linked_list_iterative:")
print(PLTIT)
print("\nprint_linked_list_recursive:")
print(PLIRT)
