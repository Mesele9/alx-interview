#!/usr/bin/python3
""" log parsing """
import sys


def print_stats(total_size, status_codes):
    """ function for printing """
    print("File size:", total_size)
    for status_code, count in sorted(status_codes.items()):
        print("{}: {}".format(status_code, count))


def main():
    """ main function """
    total_size = 0
    status_codes = {}

    try:
        file_size = 0
        status_code = 0

        for line_num, line in enumerate(sys.stdin, 1):
            parts = line.strip().split()
            if len(parts) == 9 and parts[-2].isdigit():
                file_size = int(parts[-1])
                status_code = int(parts[-2])

            total_size += file_size

            if status_code in status_codes:
                status_codes[status_code] += 1
            else:
                status_codes[status_code] = 1

            if line_num % 10 == 0:
                print_stats(total_size, status_codes)

        print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        sys.exit(0)


if __name__ == "__main__":
    main()

