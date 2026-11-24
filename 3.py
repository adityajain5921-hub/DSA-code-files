class BookNode:
    def __init__(self, book_id: str):
        self.book_id = book_id
        self.next = None


class BookIdLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, book_id: str) -> None:
        """Insert a new book ID at the head of the list."""
        new_node = BookNode(book_id)
        new_node.next = self.head
        self.head = new_node
        print(f'Inserted at beginning: "{book_id}"')

    def insert_at_end(self, book_id: str) -> None:
        """Insert a new book ID at the tail of the list."""
        new_node = BookNode(book_id)
        if self.head is None:
            self.head = new_node
            print(f'Inserted at end (as first item): "{book_id}"')
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        print(f'Inserted at end: "{book_id}"')

    def delete_from_beginning(self) -> str | None:
        """Remove and return the book ID at the head of the list."""
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return None

        removed_id = self.head.book_id
        self.head = self.head.next
        print(f'Deleted from beginning: "{removed_id}"')
        return removed_id

    def display(self) -> None:
        """Display all book IDs in order from head to end."""
        if self.head is None:
            print("Book ID list is empty.")
            return

        print("\n--- Library Book IDs (Head -> End) ---")
        current = self.head
        parts = []
        while current is not None:
            parts.append(f"[{current.book_id}]")
            current = current.next
        print(" -> ".join(parts) + " -> None")
        print("--------------------------------------\n")


# Example usage
if __name__ == "__main__":
    library_ids = BookIdLinkedList()

    library_ids.insert_at_end("BK-102")
    library_ids.insert_at_beginning("BK-101")
    library_ids.insert_at_end("BK-103")
    library_ids.display()

    library_ids.delete_from_beginning()
    library_ids.display()

    library_ids.insert_at_beginning("BK-100")
    library_ids.display()