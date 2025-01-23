#!/usr/bin/python3

"""
Find min operations of n H in a text file
"""


def minOperations(n) -> int:
    """
    Calculates the minimum number of operations needed to 
    result in exactly n 'H' characters in a text file,
    starting with a single 'H'. The only operations allowed are 
    Copy All and Paste.
    Args:
        n (int): The target number of 'H' characters.
    Returns:
        int: The minimum number of operations required to 
        achieve exactly n 'H' characters.
              Returns 0 if n is less than 2.
    """

    if n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
