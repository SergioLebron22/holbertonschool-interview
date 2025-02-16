#!/usr/bin/python3

"""
This module is used to parse logs. It reads logs 
from the standard input,
parses them, and prints statistics every 10 lines.
"""

# Variables
log_input = input()  # Read the first line of input
parsed_data = []  # List to store parsed data
file_size = 0  # Variable to store the total file size
status_codes = {  # Dictionary to store the count of each status code
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}

# Main loop
while log_input:
    # Loop to process 10 lines at a time
    for i in range(10):
        # Parse the data and add it to the parsed_data list
        parsed_data.append(log_input.split())
        # If the data is not complete, read the next line and
        # # continue to the next iteration
        if len(parsed_data[i]) != 9:
            log_input = input()
            continue
        # Add the file size to the total
        file_size += int(parsed_data[i][8])
        # Increment the count of the status code in the dictionary
        key = parsed_data[i][7]
        status_codes[key] += 1

    # Print the total file size
    print(f"File size: {file_size}")
    # Print the count of each status code
    for key, value in status_codes.items():
        if value != 0:
            print(f"{key}: {value}")

    # Reset the parsed_data list for the next batch of lines
    parsed_data = []
    # Read the next line of input
    log_input = input()