class LegalDocument:
    def __init__(self, doc_id, doc_type, client_name):
        self.doc_id = doc_id
        self.doc_type = doc_type
        self.client_name = client_name

    def __str__(self):
        return f"[ID: {self.doc_id}, Type: {self.doc_type}, Client: {self.client_name}]"

class Node:
    def __init__(self, document):
        self.document = document
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, document):
        """Insert a document into the BST."""
        if not self.root:
            self.root = Node(document)
            print(f"Inserted: {document}")
        else:
            self._insert(self.root, document)

    def _insert(self, current, document):
        if document.doc_id < current.document.doc_id:
            if current.left is None:
                current.left = Node(document)
                print(f"Inserted: {document}")
            else:
                self._insert(current.left, document)
        elif document.doc_id > current.document.doc_id:
            if current.right is None:
                current.right = Node(document)
                print(f"Inserted: {document}")
            else:
                self._insert(current.right, document)

    def search(self, doc_id):
        """Search for a document by its ID."""
        return self._search(self.root, doc_id)

    def _search(self, current, doc_id):
        if not current:
            return None
        if current.document.doc_id == doc_id:
            return current.document
        elif doc_id < current.document.doc_id:
            return self._search(current.left, doc_id)
        else:
            return self._search(current.right, doc_id)

# Example Usage
def demonstrate_bst():
    # Create sample documents
    doc1 = LegalDocument("W001", "will", "Yves Amigo")
    doc2 = LegalDocument("C001", "Contract", "Annah")
    doc3 = LegalDocument("W002", "will", "Musabika Fidele")

    # Initialize BST
    bst = BST()

    # Insert documents into BST
    print("Inserting documents:")
    bst.insert(doc1)
    bst.insert(doc2)
    bst.insert(doc3)

    # Search for a document
    search_id = "W002"
    print(f"\nSearching for document ID {search_id}:")
    result = bst.search(search_id)
    if result:
        print(f"Found: {result}")
    else:
        print("Document not found.")

# Run the demonstration
if __name__ == "__main__":
    demonstrate_bst()
