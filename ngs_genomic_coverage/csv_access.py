#!/usr/bin/env python3
"""Hold methods for reading and write NGS-related csv files."""
import csv
import numpy as np
from numpy import genfromtxt


class Csv_access():
    """Read and write access to loci and read files."""

    def __init__(self
                ,reads_path='.//ngs_genomic_coverage//data//reads.csv'
                ,loci_path='.//ngs_genomic_coverage//data//loci.csv'
                ,ngs_coverage_path='.//ngs_genomic_coverage//data//loci.csv'):
        """Initialize the csv accessor."""
        self._reads_path = reads_path
        self._loci_path = loci_path
        self._ngs_coverage_path = ngs_coverage_path

    def read_loci(self):
        """Read in the loci csv file."""
        loci = []

        try:
            with open(self._loci_path) as csv_file:
                read_csv = csv.reader(csv_file, delimiter=',')
                for row in read_csv:
                    loci.append(row)
            del loci[0]  # delete unneeded header information
        except Exception as e:
            print('There was an error reading the file: {}. The error is: {}'.format(self._loci_path, str(e)))

        return loci

    def read_ngs_data(self):
        """Read the NGS data from the csv file."""
        ngs_data_array = None

        try:
            with open(self._reads_path, 'r') as csv_file:
                reads = csv.reader(csv_file, delimiter=',')
                ngs_data = [[int(read[0]), int(read[1])] for read in reads if read is not None and read[0].isdigit()]
                ngs_data = sorted(ngs_data, key=lambda x: x[0], reverse=False)
                ngs_data_array = np.asarray(ngs_data, dtype=int)
            print('Done with reading next generation sequence data')
        except Exception as e:
            print('There was an error reading the file: {}. The error is: {}'.format(self._reads_path, e))
            read = None

        return ngs_data_array

    def write_loci(self, ngs_coverage_position):
        """Write to the loci file."""
        try:
            with open(self._ngs_coverage_path, "w") as csv_file:
                writer = csv.writer(csv_file)
                writer.writerows(ngs_coverage_position)
        except Exception as e:
            print('There was an error reading file: {}. The error is: {}'.format(self._ngs_coverage_path, e))
