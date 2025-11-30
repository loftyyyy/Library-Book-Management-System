# Library Book Management System

## Description

The **Library Book Management System (LBMS)** is a console-based Python program that helps manage book records in a small library. It allows users to borrow and return books while tracking their availability, providing a clean and interactive interface for library management.

---

## Features

* **Add Book Records**: Each book stores its title, author, publication year, and availability status.
* **Borrow a Book**: Marks a book as unavailable when borrowed.
* **Return a Book**: Marks a book as available when returned.
* **Display Book Information**: Shows book details and availability.
* **Interactive Menu**: Simple console-based interface for easy navigation.

---

## Object-Oriented Concepts

The system is built using **Object-Oriented Programming (OOP)** principles:

### Class: `Book`

Represents a single book in the library.

* **Attributes**:

  * `title` – The title of the book.
  * `author` – The author of the book.
  * `year_published` – Year the book was published.
  * `status` – Current availability (`available` or `unavailable`).
* **Methods**:

  * `display_info()` – Returns a string with book details and status.
  * `get_title()`, `get_author()`, `get_yearPublished()`, `get_status()` – Getters for book attributes.
  * `is_available()` – Returns `True` if the book is available.
  * `borrow_book()` – Marks the book as unavailable if it is currently available.
  * `return_book()` – Marks the book as available if it is currently unavailable.

### Class: `LBMS`

Manages the library system:

* Displays all books and borrowed books.
* Handles borrowing and returning books.
* Provides a main menu loop for user interaction.
* Clears the screen for a cleaner user experience.

---

## Installation

1. Ensure **Python 3** is installed.
2. Clone or download this repository.
3. Run the program with:

   ```bash
   python main.py
   ```

---

## Usage

1. Run the program.
2. Select an option from the main menu:

   ```
   [1] Borrow a Book
   [2] Return a Book
   [0] Exit
   ```
3. Follow prompts to borrow or return books.
4. The system shows the current list of books and their availability before performing any action.

---

## Example Interaction

```
==== LIBRARY MANAGEMENT SYSTEM ====

[1] Borrow a Book
[2] Return a Book
[0] Exit

Selection [0-2]: 1

==== Choose Your Book ====
[1] To Kill a Mockingbird (1960)
[2] 1984 (1949)
...
[0] Exit

Selection [0-20]: 1
You selected: To Kill a Mockingbird (1960) by Harper Lee
Confirm Selection? [Y/N]: Y
To Kill a Mockingbird successfully borrowed!
```

---

## License

This project is free to use for educational purposes and is open-source.

