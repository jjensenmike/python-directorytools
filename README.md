python-directorytools
======================

Python module to search through a directory

Mike Jensen (jjensen.mike [at] gmail.com)

Distributed under the PSF License: http://www.python.org/psf/license/

Originally wrote for VAVE xml feed destructor (https://github.com/votinginfoproject/VAVE)

Installation
============

Run:

python setup.py install

Examples
========

import directorytools as dt

dt.file_by_name("test.txt")

'/home/jensen/personal/python-directorysearch/testdata/test.txt'

dt.folder_list()

['/home/jensen/personal/python-directorysearch/testdata', '/home/jensen/personal/python-directorysearch/testdata/secondlevel', '/home/jensen/personal/python-directorysearch/testdata/secondlevel/thirdlevel1', '/home/jensen/personal/python-directorysearch/testdata/secondlevel/thirdlevel2']

dt.file_by_extension(".xml")

'/home/jensen/personal/python-directorysearch/testdata/test.xml'
