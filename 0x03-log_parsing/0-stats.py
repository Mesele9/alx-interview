#!/usr/bin/python3
""" log parsing """
import sys


def print_stats(total_size, status_codes):
    print("File size:", total_size)
    for status_code, count in sorted(status_codes.items()):
        print("{}: {}".format(status_code, count))


def main():
    total_size = 0
    status_codes = {}

    try:
        for line_num, line in enumerate(sys.stdin, 1):
            parts = line.split()
            if len(parts) < 9:
                continue

            try:
                file_size = int(parts[-1])
                status_code = int(parts[-2])
            except ValueError:
                continue

            total_size += file_size
            status_codes[status_code] = status_codes.get(status_code, 0) + 1

            if line_num % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        sys.exit(0)

if __name__ == "__main__":
    main()
