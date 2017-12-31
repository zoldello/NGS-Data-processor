# -*- coding: utf-8 -*-
"""Main file for program."""
from csv_access import Csv_access
from coverage import Coverage


if __name__ == '__main__':
    print("""Next-Generation Sequencing Coverage Calculator Application,
    Starting up...
    This may take a minute or two, so please be patient
    """)

    csv = Csv_access()
    ngs_reads = csv.read_ngs_data()
    coverage = Coverage(ngs_reads)
    loci = csv.read_loci()
    ngs_coverage = [['position', 'coverage']]
    i = 0

    for locus in loci:
        if not locus:
            continue

        position = int(locus[0]) if locus[0] is not None and type(locus[0]) == str and locus[0].isdigit else -1
        i += 1

        if position == -1:  # sign position is invalid
            continue

        locus_coverage = [position, coverage.get_coverage(position)]
        ngs_coverage.append(locus_coverage)
        print("Finished loci position: {}".format(i))

    csv.write_loci(ngs_coverage)
