class LegalDocument:
    def __init__(self, doc_id, doc_type):
        self.doc_id = doc_id
        self.doc_type = doc_type
    def __str__(self):
        return f"[{self.doc_id} - {self.doc_type}]"

class Node:
    def __init__(self, document):
        self.document = document
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, document):
        new_node = Node(document)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current, result = self.head, []
        while current:
            result.append(str(current.document))
            current = current.next
        return " -> ".join(result)

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, document):
        new_node = Node(document)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def display(self):
        if not self.head:
            return "Empty List"
        current, result = self.head, []
        while True:
            result.append(str(current.document))
            current = current.next
            if current == self.head:
                break
        return " -> ".join(result) + " -> (Back to Head)"

doc1 = LegalDocument("W001", "Will")
doc2 = LegalDocument("C001", "Contract")
doc3 = LegalDocument("W002", "Will")

ll = LinkedList()
ll.insert(doc1)
ll.insert(doc2)
ll.insert(doc3)
print("Linked List:", ll.display())

cll = CircularLinkedList()
cll.insert(doc1)
cll.insert(doc2)
cll.insert(doc3)
print("Circular Linked List:", cll.display())
