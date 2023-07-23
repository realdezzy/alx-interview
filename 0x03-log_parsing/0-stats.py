#!/usr/bin/python3
""" Display stats logging
"""
import sys
count = 0
total_size = 0
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
keys = statuses.keys()


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
            value = values.split()
            status = value[7]
            size = int(value[8])
            if status in keys:
                statuses[status] += 1
                total_size += size
                count += 1

            else:
                continue

    except KeyboardInterrupt:
        pass

    finally:
        print_values()
