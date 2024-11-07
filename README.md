# **Integer Type Detector** 🔢

## Description 💡

This Python function `detecting_integer(list)` is designed to classify each integer in a list as either **positive**, **negative**, or **zero**. The function iterates through the list and returns a new list with the classification for each number.

For example:
- **Input**: 
  - `list`: `[1, -5, 0, 12, -3]`
- **Output**: `["positive", "negative", "zero", "positive", "negative"]`

### Why is it Useful? 🤔
This function is useful for categorizing integers in datasets or lists, helping with analysis or data cleaning. It's ideal for use in preprocessing steps for tasks where the classification of numbers into specific categories is required.

---

## **Features** ✨

- **Zero Detection**: Detects and labels zeros as "zero" 🔢.
- **Positive Detection**: Detects and labels positive numbers as "positive" ➕.
- **Negative Detection**: Detects and labels negative numbers as "negative" ➖.
- **Efficient Iteration**: Processes each number in the list and returns a classification with minimal complexity.

---

## **Function** 💻

```python
def detecting_integer(list):
    # Initialize an empty list to store the detected types of integers
    type_integer = []

    # Iterate over each index of the input list
    for i in range(len(list)):
        # Check if the current integer is zero
        if list[i] == 0:
            # Append "zero" to the type_integer list
            type_integer.append("zero")
        # Check if the current integer is positive
        elif list[i] > 0:
            # Append "positive" to the type_integer list
            type_integer.append("positive")
        # If the integer is neither zero nor positive, it must be negative
        else:
            # Append "negative" to the type_integer list
            type_integer.append("negative")

    # Return the list of detected types
    return type_integer
