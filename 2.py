class TicketQueueArray:
    def __init__(self, capacity: int = 5):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0.")
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_full(self) -> bool:
        return self.size == self.capacity

    def is_empty(self) -> bool:
        return self.size == 0

    def enqueue(self, customer: str) -> bool:
        """Add a customer to the rear of the queue."""
        if self.is_full():
            print(f'Queue is full! Could not add "{customer}".')
            return False
        self.rear = (self.rear + 1) % self.capacity
        self.array[self.rear] = customer
        self.size += 1
        print(f'Enqueued: "{customer}"')
        return True

    def dequeue(self) -> str | None:
        """Serve and remove the customer at the front of the queue."""
        if self.is_empty():
            print("No customers in the queue to serve.")
            return None
        customer = self.array[self.front]
        self.array[self.front] = None  # Clear slot for cleanliness
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        print(f'Dequeued (served): "{customer}"')
        return customer

    def display(self) -> None:
        """Display customers currently waiting from front to rear."""
        if self.is_empty():
            print("Queue is empty.")
            return
        print("\n--- Ticket Counter Queue (Front -> Rear) ---")
        for i in range(self.size):
            idx = (self.front + i) % self.capacity
            tags = []
            if i == 0:
                tags.append("FRONT / Serving next")
            if i == self.size - 1:
                tags.append("REAR / Last arrived")
            label = f"  <-- {' | '.join(tags)}" if tags else ""
            print(f"{i + 1}. {self.array[idx]}{label}")
        print("--------------------------------------------\n")


# Example usage
if __name__ == "__main__":
    counter = TicketQueueArray(capacity=4)

    counter.enqueue("Aarav")
    counter.enqueue("Meera")
    counter.enqueue("Rohan")
    counter.display()

    counter.dequeue()
    counter.display()

    counter.enqueue("Ananya")
    counter.enqueue("Kabir")
    counter.enqueue("Vikram")  # Demonstrates queue full handling
    counter.display()