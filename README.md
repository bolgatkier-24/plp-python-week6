# PLP Python Week 6 Assignment

## Files Overview
* **safe_tools.py**: Contains three error-handled functions (`safe_divide`, `safe_number`, and `get_field`) designed to prevent crashes.
* **unbreakable.py**: Implements robust input handling to ensure safe execution when dealing with unexpected user input.

## Reflection Question
**Why can the if check not catch "abc" on its own?**
An `if` statement relying solely on string methods (like `.isdigit()`) can easily miss edge cases or fail to handle unexpected data types robustly across different contexts. Exception handling (`try-except`) is superior because it allows the program to attempt the operation directly and gracefully catch whatever error (`ValueError`, `TypeError`, etc.) occurs, rather than trying to predict every malformed input beforehand.
