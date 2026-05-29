"""
Module 1 Assignment: Introduction to DSA & Python Collections
Fill in the blanks/complete the functions below according to the docstrings.
"""

from collections import Counter, deque
from typing import List, Set, Dict, Tuple, Any

# =====================================================================
# SECTION 1: Understanding Data Structures & Built-in Collections
# =====================================================================

def analyze_text(text: str) -> Tuple[int, Dict[str, int], List[str]]:
    """
    Analyze a given string to understand built-in Python collections.
    
    Tasks:
    1. Count the total number of characters (including spaces).
    2. Count the frequency of each character using a dictionary.
    3. Return a list of all unique words in the text (lowercased, sorted alphabetically).
    
    Example:
        "Apple apple" -> (11, {'A': 1, 'p': 4, 'l': 2, 'e': 2, ' ': 1, 'a': 1}, ['apple'])
    """
    # TODO: Implement this function
    pass


def manipulate_tuple_and_set(items: List[Any]) -> Tuple[Tuple[Any, ...], Set[Any]]:
    """
    Demonstrate mutability vs immutability concepts.
    
    Tasks:
    1. Convert the input list into an immutable tuple.
    2. Convert the input list into a set to remove all duplicates.
    
    Returns:
        A tuple containing (immutable_tuple, unique_set)
    """
    # TODO: Implement this function
    pass


# =====================================================================
# SECTION 2: Simulating Abstract Data Types (ADTs)
# =====================================================================

class SimpleQueueADT:
    """
    Simulate a Queue ADT (First-In, First-Out) using Python's deque.
    """
    def __init__(self):
        # Initialize the underlying collection here
        self._items = deque()

    def enqueue(self, item: Any) -> None:
        """Add an item to the back of the queue."""
        # TODO: Implement this
        pass

    def dequeue(self) -> Any:
        """Remove and return the item from the front of the queue. 
        Raise IndexError if empty."""
        # TODO: Implement this
        pass

    def is_empty(self) -> bool:
        """Return True if the queue is empty, False otherwise."""
        # TODO: Implement this
        pass


class SimpleGraphADT:
    """
    Simulate an Undirected Graph ADT using an Adjacency List (Dictionary of Sets).
    """
    def __init__(self):
        # Keys are vertices, values are sets of neighboring vertices
        self.graph: Dict[Any, Set[Any]] = {}

    def add_vertex(self, vertex: Any) -> None:
        """Add a new vertex to the graph if it doesn't exist."""
        # TODO: Implement this
        pass

    def add_edge(self, v1: Any, v2: Any) -> None:
        """Add an undirected edge between v1 and v2. 
        Automatically add vertices if they don't exist."""
        # TODO: Implement this
        pass

    def get_neighbors(self, vertex: Any) -> Set[Any]:
        """Return the set of neighbors for a given vertex."""
        # TODO: Implement this
        pass
