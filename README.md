# Python Logic & Flow Control Projects

A collection of beginner to intermediate Python scripts focused on mastering core programming concepts like data types, loops, and conditional logic.

## 🚀 Projects Included

### 1. Smart Tip Calculator
A utility script designed to handle bill splitting with custom tip percentages.

*   **Key Concepts:** User input handling, type casting (floats/ints), arithmetic operations, and string formatting.
*   **How it works:** 
    *   Takes the total bill and the desired tip percentage.
    *   Calculates the total amount per person.
    *   Outputs a clean, formatted currency value.

### 2. Automated "Guess the Number" Game
A classic CLI-based game where the user competes against the computer.

*   **Key Concepts:** The `random` library, `while` loops, nested `if/else` statements, and attempt tracking.
*   **Features:**
    *   Generates a random integer between 1 and 100.
    *   Limits the player to 7 attempts.
    *   Provides "Too High" or "Too Low" feedback.
    *   Includes a "Play Again" loop to restart the game without exiting the script.

# Persistent Task Manager (CLI)

A Python-based To-Do List application that uses JSON for data persistence, ensuring tasks are saved across sessions.

## 🚀 Features
- **Data Persistence:** Uses the `json` library to store tasks in a local file (`task.json`).
- **Error Resilience:** Implements `try/except` blocks to handle missing files or corrupted data.
- **Full CRUD Logic:** Supports Adding, Viewing, and Removing tasks with automatic index handling.
- **Formatted Storage:** Saves data with indentation for better readability.

## 🛠️ Technical Concepts
*   **File I/O:** Reading from and writing to local files using Python's `with open()` context managers.
*   **JSON Serialization:** Converting Python lists into JSON format for storage.
*   **Exception Handling:** Managing `FileNotFoundError`, `JSONDecodeError`, and `ValueError`.
*   **List Manipulation:** Using `enumerate()` for user-friendly indexing and `pop()` for item removal.
