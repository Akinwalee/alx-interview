#!/usr/bin/python3
"""Generate logs stats"""

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
        if count != 0:
            print(f"{code}: {count}")    


def process_lines(input_stream):
    """
    Processes lines from the input stream and
    counts file sizes and status codes.

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
        parts = parts[::-1]

        if len(parts) > 2:
            counter += 1

            if counter <=10:
                file_size = int(parts[0])
                status_code = parts[1]

                total_file_size += file_size

            if status_code in status_codes.key():
                status_codes[status_code] += 1

            if counter == 10:
                print_message(status_codes, total_file_size)
                counter = 0

    return status_codes, total_file_size


def main():
    """
    Main function to run the script.
    """
    status_codes, total_file_size = {}, 0
    try:
        status_codes, total_file_size = process_lines(sys.stdin)
    finally:
        print_message(status_codes, total_file_size)


if __name__ == "__main__":
    main()
