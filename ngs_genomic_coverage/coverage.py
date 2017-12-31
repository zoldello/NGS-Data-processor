#!/usr/bin/env python3
"""Hold functionality for getting coverage information ."""


class Coverage():
    """Coverage functionality."""

    def __init__(self, ngs_data):
        """Initialize coverage class."""
        self._ngs_data = ngs_data

    def get_coverage(self, position):
        """Get the coverage based on position."""
        if (not self._ngs_data.any()):
            return 0

        ngs_data_length = len(self._ngs_data)
        first = 0
        last = ngs_data_length - 1
        midpoint = 0
        index = 0

        #  binary search
        while first <= last:
            midpoint = (first + last) // 2
            start = self._ngs_data[midpoint][0]
            start_next = self._ngs_data[midpoint + 1][0] if midpoint + 1 < ngs_data_length else None

            if (start_next is None or position < start_next) and position >= start:
                index = midpoint
                break
            else:
                if position < self._ngs_data[midpoint][0]:
                    last = midpoint - 1
                else:
                    first = midpoint + 1

        # further performace boost
        ngs_reduced = [ngs for ngs in self._ngs_data[0: midpoint+1] if ngs[0] + ngs[1] >= position]
        coverage = 0

        for read in ngs_reduced:
            start = read[0]
            max = read[0] + read[1] - 1

            coverage += 1 if position >= start and position <= max else 0

        return coverage
