#!/usr/bin/python3
"""Input stats"""
import sys

stats = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
sizes = [0]


def print_stats():
    """
    Prints the accumulated statistics of file sizes and status code counts.

    The function prints the total file size and the count of each status code
    that has been recorded. The status codes are printed in ascending order.

    The function assumes the existence of two global variables:
    - sizes: A list of integers representing file sizes.
    - stats: A dictionary where keys are status codes (as strings) and values
      are the counts of occurrences of each status code.
    """
    print('File size: {}'.format(sum(sizes)))
    for s_code, count in sorted(stats.items()):
        if count:
            print('{}: {}'.format(s_code, count))


try:
    for i, line in enumerate(sys.stdin, start=1):
        matches = line.rstrip().split()
        try:
            status_code = matches[-2]
            file_size = matches[-1]
            if status_code in stats.keys():
                stats[status_code] += 1
            sizes.append(int(file_size))
        except Exception:
            pass
        if i % 10 == 0:
            print_stats()
    print_stats()
except KeyboardInterrupt:
    print_stats()
    raise