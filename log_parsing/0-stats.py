#!/usr/bin/python3
"""
This script reads from standard input and processes log entries to compute
the total file size and the count of specific HTTP status codes.
The script expects log entries in the following format:
<IP Address> - [<Date>] "GET /projects/260 HTTP/1.1" <Status Code> <File Size>
The script maintains a running total of the file size and counts occurrences
of the following HTTP status codes: 200, 301, 400, 401, 403, 404, 405, 500.
Every 10 lines, the script prints the current total file size and the counts
of the status codes that have been encountered so far.
If the script is interrupted (e.g., via a keyboard interrupt), it will print
the final totals before exiting.
Attributes:
    i (int): Line counter.
    FileSize (int): Total file size of processed log entries.
    STATUS (dict): Dictionary to store counts of specific HTTP status codes.
Usage:
    cat log_file | ./0-stats.py
"""

import sys


i = 0
FileSize = 0
STATUS = {'200': 0, '301': 0,
          '400': 0, '401': 0,
          '403': 0, '404': 0,
          '405': 0, '500': 0}
try:
    for line in sys.stdin:
        i += 1
        sp = line.split(' ')
        if len(sp) > 2:
            FileSize += int(sp[-1])
            if sp[-2] in STATUS:
                STATUS[sp[-2]] += 1
        if i % 10 == 0:
            print("File size: {}".format(FileSize))
            for key, value in sorted(STATUS.items()):
                if value != 0:
                    print("{}: {}".format(key, value))
finally:
    print("File size: {}".format(FileSize))
    for key, value in sorted(STATUS.items()):
        if value != 0:
            print("{}: {:d}".format(key, value))