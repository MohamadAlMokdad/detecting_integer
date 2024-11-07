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

