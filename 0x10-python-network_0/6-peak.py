#!/usr/bin/python3
"""
An element in the list is said to be peak if
it is NOT smaller than its neighbors.
"""


def find_peak(E):
    """find pick element"""
    if E == []:
        return None

    def recursive(E, left=0, right=len(E) - 1):
        """helper recursive function"""

        mid = (left + right) // 2

        # check if the middle element is greater than its neighbors
        if ((mid == 0 or E[mid - 1] <= E[mid]) and
                (mid == len(E) - 1 or E[mid + 1] <= E[mid])):
            return E[mid]

        # If the left neighbor of `mid` is greater than the middle element,
        # find the peak recursively in the left sublist
        if mid - 1 >= 0 and E[mid - 1] > E[mid]:
            return recursive(E, left, mid - 1)

        # If the right neighbor of `mid` is greater than the middle element,
        # find the peak recursively in the right sublist
        return recursive(E, mid + 1, right)

    return recursive(E)
