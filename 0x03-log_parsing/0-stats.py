#!/usr/bin/python3

import sys


def print_message(status_codes, total_file_size):
    """
    Prints the total file size and counts of status codes.

    Args:
        status_codes (dict): Dictionary of status codes and their counts.
        total_file_size (int): Total size of the files processed.
    """
    print(f"File size: {total_file_size}")
    for code, count in sorted(status_codes.items()):
        if count:
            print(f"{code}: {count}")


def process_lines(input_stream):
    """
    Processes lines from the input stream and counts file sizes and status codes.

    Args:
        input_stream: Stream from which to read lines.
    """
    total_file_size = 0
    status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0,
    }
    
    counter = 0

    for line in input_stream:
        parts = line.split()
        if len(parts) > 2:
            file_size, status_code = int(parts[0]), parts[1]
            total_file_size += file_size
            
            if status_code in status_codes:
                status_codes[status_code] += 1

            counter += 1

            if counter == 10:
                print_message(status_codes, total_file_size)
                counter = 0

    return status_codes, total_file_size


def main():
    """
    Main function to run the script.
    """
    try:
        status_codes, total_file_size = process_lines(sys.stdin)
    finally:
        print_message(status_codes, total_file_size)


if __name__ == "__main__":
    main()