=================================
NGS Genomic Coverage Application
=================================

This code calculates the genomic coverage for a given data set.


Python Version
----------------
This was built using Python 3.6 on Linux (Ubuntu). However, in theory, it should work with Python 2.7 and with Windows and Mac. However, these were not tested


How to run the code
---------------------
Open up the codebase and go to the directory: ngs_genomic_coverage/ngs_genomic_coverage. Next, run this:

**python3  ngs_genomic_coverage.py**

*"python" rather than "python3" may be needed on Window*

**Note, it may take about 5 minutes for the application to finish. The console gives you progress updates**

Code
-----
Most of the files are bioler-plate-code created by cookiecutter. The important parts of the application are located in **ngs_genomic_coverage/ngs_genomic_coverage** folder.
Here are the files:

* **coverage.py**: This hold code for calculating Coverage
* **csv_access**: Used for reading and writing to csv files
* **ngs_genomics_coverage**: This is the main code. It is an orchestrator that calls classes and uses them to drive the application

The folder ngs_genomic_coverage/ngs_genomic/data as it name implies hold data related to the application. Here are files in the folder:

- **loci.csv**: Holds the position of interest whose coverage need to be determined.
- **reads.csv**: Holds the Next generation sequences reads.
- **test_loci.csv**: Test file similar in structure to loci.csv (but not content.)
- **test_reads.csv**: Test file similar in structure to reads.csv (but not content.)

Algorithm
--------------------
1. Read in the next generation sequencing data
2. Sort the next generation sequencing data on start-field (necessary for search) in ascending order
3. Do a binary search for the maximum row-index where start-field is less than or equal to position (the next row is either None or start-field is great than position)
4. Eliminate all rows above the index from step 3.
5. From Step 4, eliminate rows whose sum of start and length is great than the position-field
6. Calculate coverage
7. Repeat for each position-field


Run-time performance and speed enhancements
--------------------------------------------
Here is a run-time analysis of major parts of the application

- **coverage.py**: Has a Binary search so has a performance of: **O(logn)**. There is another reduction of data performed after the binary search (elimate entrys where the sum of the start and length is great than or equals to position.) However, it is not significant since it is O(logn) was done on the data already.
- **csv_access**: Reading in the next generation data takes O(n). Sorting it takes **O(nlogn)**. It also takes **O(nlogn)** to write to and read from the csv file
- **ngs_genomics_coverage**: This does not do much other than call other methods. It only loops on the loci, which is much smaller than the next generation data; so is not significant

The application itself runs in **O(n)**, since this is the most significant. However, the coverage calculations take **O(nlogn)**, since a binary search is used.

I used numpy's array to handle hold the next generation sequence data. It is much faster and less memory intensive than Python's Native List object.




Credits
---------
Philip Adenekan wrote this code and received no assistance other than from Machiej who explained coverage.

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackages

Licence
--------
Harvard University staff  may use this as they see fit to critique the author. 
