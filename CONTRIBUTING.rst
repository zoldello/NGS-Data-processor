.. highlight:: shell

============
Contributing
============

This was made only by Philip Adenekan and contributions are not accepted.


Get Started!
------------

Ready to contribute? Here's how to set up `ngs_genomic_coverage` for local development.

1. Fork the `ngs_genomic_coverage` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/ngs_genomic_coverage.git

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development::

    $ mkvirtualenv ngs_genomic_coverage
    $ cd ngs_genomic_coverage/
    $ python setup.py develop

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8 and the tests, including testing other Python versions with tox::

    $ flake8 ngs_genomic_coverage tests
    $ python setup.py test or py.test
    $ tox

   To get flake8 and tox, just pip install them into your virtualenv.

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 2.6, 2.7, 3.3, 3.4 and 3.5, and for PyPy. Check
   https://travis-ci.org/zoldello/ngs_genomic_coverage/pull_requests
   and make sure that the tests pass for all supported Python versions.

Tips
----

To run a subset of tests::


    $ python -m unittest tests.test_ngs_genomic_coverage
