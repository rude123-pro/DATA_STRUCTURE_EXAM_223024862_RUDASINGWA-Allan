class Document:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def __repr__(self):
        return f"{self.name} ({self.priority})"

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left].priority > arr[largest].priority:
        largest = left

    if right < n and arr[right].priority > arr[largest].priority:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def build_heap(documents):
    n = len(documents)

    for i in range(n // 2 - 1, -1, -1):
        heapify(documents, n, i)

    return documents

def print_heap_diagram(heap):
    """
    Prints the heap visually in a diagram-like tree structure.
    """
    n = len(heap)
    if n == 0:
        print("Heap is empty.")
        return

    # Prepare the output layers
    levels = []
    depth = 0
    index = 0
    while index < n:
        level_nodes = 2 ** depth  # Number of nodes at this level
        current_level = heap[index:index + level_nodes]
        levels.append(current_level)
        index += level_nodes
        depth += 1

    # Calculate maximum width for the heap diagram
    max_width = 4 * (2 ** (len(levels) - 1)) - 1

    # Print each level with connections
    for i, level in enumerate(levels):
        # Create the node line
        node_line = ""
        gap = (max_width // (2 ** i)) // 2
        for node in level:
            node_line += f"{str(node).center(gap)}"
        print(node_line.center(max_width))

        # Add connections (except for the last level)
        if i < len(levels) - 1:
            connector_line = ""
            for _ in range(len(level)):
                connector_line += "/".center(gap)
                connector_line += "\\".center(gap)
            print(connector_line.center(max_width))

# Example data
documents = [
    Document("Will_1", 1),
    Document("Contract_1", 2),
    Document("Will_2", 3),
    Document("Contract_2", 2),
    Document("Urgent_Contract", 5)
]

# Build the heap
print("Building the heap...")
heap = build_heap(documents)

print("\nHeap Diagram:")
print_heap_diagram(heap)
