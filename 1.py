class ReturnedBookStack:
    def __init__(self):
        self._stack = []

    def return_book(self, book_title: str) -> None:
        """Push: Place a newly returned book on top of the stack."""
        self._stack.append(book_title)
        print(f'Returned (pushed): "{book_title}"')

    def arrange_book(self) -> str | None:
        """Pop: Take the top book off the stack to arrange on shelves."""
        if self.is_empty():
            print("No returned books in the stack to arrange.")
            return None
        book = self._stack.pop()
        print(f'Arranged (popped): "{book}"')
        return book

    def top_book(self) -> str | None:
        """Peek: View the next book to be arranged without removing it."""
        if self.is_empty():
            print("The returned book stack is empty.")
            return None
        top = self._stack[-1]
        print(f'Next book to arrange (top): "{top}"')
        return top

    def display_stack(self) -> None:
        """Display all books currently in the stack from top to bottom."""
        if self.is_empty():
            print("Stack is empty.")
            return
        print("\n--- Returned Books Stack (Top -> Bottom) ---")
        for index, book in enumerate(reversed(self._stack), start=1):
            marker = " <-- TOP (Next to arrange)" if index == 1 else ""
            print(f"{index}. {book}{marker}")
        print("-------------------------------------------\n")

    def is_empty(self) -> bool:
        return len(self._stack) == 0


# Example usage
if __name__ == "__main__":
    returned_books = ReturnedBookStack()

    returned_books.return_book("Clean Code")
    returned_books.return_book("The Pragmatic Programmer")
    returned_books.return_book("Designing Data-Intensive Applications")

    returned_books.display_stack()
    returned_books.top_book()

    returned_books.arrange_book()
    returned_books.display_stack()