#!/usr/bin/env python3
""" Display stats logging
"""
import sys
import re

count = 0
size = 0
statuses = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0,
}
regx = (r"(\d{1,3}\.){3}\d{1,3} - \[\d{4}-\d{2}-\d{2} (\d{2}:)"
        r"{2}\d{2}\.\d{6}\] \"GET /projects/260 HTTP/1.1\" \d{3} \d{1,4}")


def print_values():
    """ Format and print stats to stdout.
    """
    print(f"File size: {size}")
    for k, v in statuses.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    try:
        for values in sys.stdin:
            if (count > 0 and count % 10 == 0):
                print_values()
            if re.search(regx, values):
                value = values.split()
                statuses[value[7]] += 1
                size += int(value[8])
                count += 1

            else:
                continue

    except KeyboardInterrupt:
        pass

    finally:
        print_values()
