#!/usr/bin/python3
""" log parsing """
import sys


def print_stats(lines, total_file_size, status_codes):
    print("File size:", total_file_size)
    for status_code in sorted(status_codes):
        if status_codes[status_code] > 0:
            print("{}: {}".format(status_code, status_codes[status_code])


def main():
    total_file_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}
    lines = []

    try:
        for line in sys.stdin:
            parts = line.strip().split()
            if len(parts) != 9:
                continue

            status_code, file_size = int(parts[-2]), int(parts[-1])
            total_file_size += file_size
            status_codes[status_code] += 1
            lines.append(line)

            if len(lines) == 10:
                print_stats(lines, total_file_size, status_codes)
                lines = []

    except KeyboardInterrupt:
        print_stats(lines, total_file_size, status_codes)


if __name__ == "__main__":
    main()
