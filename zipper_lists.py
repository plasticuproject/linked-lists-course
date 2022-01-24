"""zipper_lists.py"""
from timeit import timeit
from typing import Optional, List, Tuple


class Node:  # pylint: disable=too-few-public-methods
    """Node class for linked list structure."""

    def __init__(self, val: Optional[str]) -> None:
        self.val = val
        self.next: Optional[Node] = None


def construct_linked_lists() -> Tuple[Node, ...]:
    """Used to construct linked lists for tests."""

    # LINKED LISTS
    # A -> B -> C -> D -> None
    # Q -> R -> None

    _a = Node("A")
    _b = Node("B")
    _c = Node("C")
    _d = Node("D")
    _q = Node("Q")
    _r = Node("R")
    _a.next = _b
    _b.next = _c
    _c.next = _d
    _q.next = _r
    return _a, _b, _c, _d, _q, _r


def zipper_lists_iterative(head_one: Optional[Node],
                           head_two: Optional[Node]) -> Optional[Node]:
    """My method of iterating through two linked lists, mutating the
    first list to be zipped with the second, regardless which is
    longer/shorter, and returning the mutated first list."""
    if not head_one and head_two:
        return head_two
    if head_one and not head_two:
        return head_one
    current_one = head_one
    current_two = head_two
    next_one: Optional[Node] = None
    next_two: Optional[Node] = None
    previous_one: Optional[Node] = None
    while current_one and current_two:
        previous_one = current_one
        next_one = current_one.next
        next_two = current_two.next
        current_one.next = current_two
        current_two.next = next_one
        current_one = next_one
        current_two = next_two
    while current_two:
        if previous_one:
            current_one = previous_one.next
            previous_one = previous_one.next
        if current_one:
            current_one.next = current_two
        current_two = current_two.next
    return head_one


def alvin_zipper_lists_iterative(head_one: Optional[Node],
                                 head_two: Optional[Node]) -> Optional[Node]:
    """Alvin's method of iterating through two linked lists, mutating
    the first list to be zipped with the second, regardless which is
    longer/shorter, and returning the mutated first list."""
    if not head_one and head_two:
        return head_two
    if head_one and not head_two:
        return head_one
    current_one: Optional[Node] = None
    current_two: Optional[Node] = None
    if head_one:
        tail = head_one
        current_one = head_one.next
        current_two = head_two
    count: int = 0
    while current_one and current_two:
        if count % 2 == 0:
            tail.next = current_two
            current_two = current_two.next
        else:
            tail.next = current_one
            current_one = current_one.next
        tail = tail.next
        count += 1
    if current_one:
        tail.next = current_one
    if current_two:
        tail.next = current_two
    return head_one


def zipper_lists_recursive(head_one: Optional[Node],
                           head_two: Optional[Node]) -> Optional[Node]:
    """Recursive method of traversing through two linked lists, mutating
    the first list to be zipped with the second, regardless which is
    longer/shorter, and returning the mutated first list."""
    if not head_one and not head_two:
        return None
    if not head_one:
        return head_two
    if not head_two:
        return head_one
    next_one = head_one.next
    next_two = head_two.next
    head_one.next = head_two
    head_two.next = zipper_lists_recursive(next_one, next_two)
    return head_one


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


a, b, c, d, q, r = construct_linked_lists()
assert not zipper_lists_iterative(None, None)
assert zipper_lists_iterative(a, None) == a
assert zipper_lists_iterative(None, a) == a
e = zipper_lists_iterative(a, q)
assert linked_list_values_iterative(e) == ["A", "Q", "B", "R", "C", "D"]
a, b, c, d, q, r = construct_linked_lists()
f = zipper_lists_iterative(q, a)
assert linked_list_values_iterative(f) == ["Q", "A", "R", "B", "C", "D"]

a, b, c, d, q, r = construct_linked_lists()
assert not alvin_zipper_lists_iterative(None, None)
assert alvin_zipper_lists_iterative(a, None) == a
assert alvin_zipper_lists_iterative(None, a) == a
e = alvin_zipper_lists_iterative(a, q)
assert linked_list_values_iterative(e) == ["A", "Q", "B", "R", "C", "D"]
a, b, c, d, q, r = construct_linked_lists()
f = alvin_zipper_lists_iterative(q, a)
assert linked_list_values_iterative(f) == ["Q", "A", "R", "B", "C", "D"]

a, b, c, d, q, r = construct_linked_lists()
assert not zipper_lists_recursive(None, None)
assert zipper_lists_recursive(a, None) == a
assert zipper_lists_recursive(None, a) == a
e = zipper_lists_recursive(a, q)
assert linked_list_values_iterative(e) == ["A", "Q", "B", "R", "C", "D"]
a, b, c, d, q, r = construct_linked_lists()
f = zipper_lists_recursive(q, a)
assert linked_list_values_iterative(f) == ["Q", "A", "R", "B", "C", "D"]

# TIME TESTS
a, b, c, d, q, r = construct_linked_lists()
print("\nzipper_lists_iterative:")
print(timeit(lambda: zipper_lists_iterative(a, q), number=1))

a, b, c, d, q, r = construct_linked_lists()
print("\nalvin_zipper_lists_iterative:")
print(timeit(lambda: alvin_zipper_lists_iterative(a, q), number=1))

a, b, c, d, q, r = construct_linked_lists()
print("\nzipper_lists_recursive:")
print(timeit(lambda: zipper_lists_recursive(a, q), number=1))
