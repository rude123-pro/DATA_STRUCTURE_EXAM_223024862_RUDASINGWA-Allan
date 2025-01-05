class Order:
    def __init__(self, order_id, doc_type, client_name):
        self.order_id = order_id
        self.doc_type = doc_type
        self.client_name = client_name
    def __str__(self):
        return f"Order ID: {self.order_id}, Type: {self.doc_type}, Client: {self.client_name}"

class CircularQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [None] * max_size
        self.front = self.rear = -1

    def enqueue(self, order):
        if (self.rear + 1) % self.max_size == self.front: 
            print("Queue is full. Overwriting the oldest order.")
            self.front = (self.front + 1) % self.max_size
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = order
        if self.front == -1: 
            self.front = 0

    def dequeue(self):
        if self.front == -1:
            return None
        order = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size
        return order

    def display(self):
        if self.front == -1: 
            print("Queue is empty.")
            return
        i = self.front
        print("Current orders in the queue:")
        while True:
            print(self.queue[i])
            if i == self.rear:
                break
            i = (i + 1) % self.max_size

def demonstrate_circular_queue():
    order1 = Order("O001", "Will", "Allan RUDASINGWA")
    order2 = Order("O002", "Contract", "Yves Amigo")
    order3 = Order("O003", "Will", "Manzi Frank")
    order4 = Order("O004", "Contract", "Wilson MUGABO")

    cq = CircularQueue(3)

    cq.enqueue(order1)
    cq.enqueue(order2)
    cq.enqueue(order3)
    cq.enqueue(order4)  

    cq.display()

    removed_order = cq.dequeue()
    print(f"Removed Order: {removed_order}")
    cq.display()

if __name__ == "__main__":
    demonstrate_circular_queue()
