"""reverse_list.py"""
from timeit import timeit
from typing import Optional, List


class Node:  # pylint: disable=too-few-public-methods
    """Node class for linked list structure."""

    def __init__(self, val: Optional[str]) -> None:
        self.val = val
        self.next: Optional[Node] = None


def reverse_list_iterative(head: Optional[Node]) -> Optional[Node]:
    """Iteratively traverse through and mutate linked list to
    reverse the order. Returns new head Node."""
    current = head
    previous_node: Optional[Node] = None
    next_node: Optional[Node] = None
    while current:
        next_node = current.next
        current.next = previous_node
        previous_node = current
        current = next_node
    return previous_node


def reverse_list_recursive(
        head: Optional[Node],
        previous_node: Optional[Node] = None) -> Optional[Node]:
    """recursively traverse through and mutate linked list to
    reverse the order. Returns new head Node."""
    if not head:
        return previous_node
    next_node = head.next
    head.next = previous_node
    return reverse_list_recursive(next_node, head)


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
def linked_list_values_iterative(head: Optional[Node]) -> List[str]:
    """Iterate through linked list and return array of all Node values."""
    current = head
    values: List[str] = []
    while current:
        if current.val:
            values.append(current.val)
        current = current.next
    return values


assert not reverse_list_iterative(None)
f = reverse_list_iterative(a)
assert linked_list_values_iterative(f) == ["D", "C", "B", "A"]
f = reverse_list_iterative(f)
assert linked_list_values_iterative(a) == ["A", "B", "C", "D"]
f = reverse_list_iterative(d)
assert linked_list_values_iterative(d) == ["D"]

assert not reverse_list_recursive(None)
f = reverse_list_recursive(a)
assert linked_list_values_iterative(f) == ["D", "C", "B", "A"]
f = reverse_list_recursive(f)
assert linked_list_values_iterative(a) == ["A", "B", "C", "D"]
f = reverse_list_recursive(d)
assert linked_list_values_iterative(d) == ["D"]

# TIME TESTS
print("\nreverse_list_iterative:")
print(timeit(lambda: reverse_list_iterative(a), number=1000000))
print("\nreverse_list_recursive:")
print(timeit(lambda: reverse_list_recursive(a), number=1000000))
