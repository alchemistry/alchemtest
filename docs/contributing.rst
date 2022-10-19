.. -*- coding: utf-8 -*-
   
.. _contributing:

Contributing new data sets
==========================

We are looking for new data sets. Please read the following and
consider contributing data; details are described under
:ref:`process`.


Types of systems
----------------

The ideal set of files would be something like the GROMACS dataset for
alchemtest :mod:`alchemtest.gmx`: benzene in water for 1...10 ns per
window, with :math:`\partial H/\partial\lambda` saved every 10 ps. For
GROMACS we tend to put each lambda in a separate directory (see the
directory layout in `alchemtest/gmx/benzene`_) but you should provide
files that are typical of how the specific code is run.

.. _`alchemtest/gmx/benzene`:
   https://github.com/alchemistry/alchemtest/tree/master/src/alchemtest/gmx/benzene

Data set description
--------------------

For your data set, you should be able to include the following in a 
brief description (which will become part of the data set and the
documentation as described in more detail in :ref:`process`):

* Include the value(s) that you get when analyzing the data set 
  yourself so that we know the ground truth. 
  
  It is very helpful if you include a brief explanation of how you 
  analyze the data with alchemlyb or your own tool (show Python commands 
  or the full command with options so that one can reproduce the 
  analysis if necessary).  
* State how the data set was generated. Include the temperature.
* Comment on what to look out for in the output files, e.g., special
  sampling options. 
* For **new file formats:** Include information about the file format
  definition, such as *links* or *paper citations*.

In general, follow the example of the existing data sets (especially
similar data sets or for the same MD/MC code) and discuss the specfics
on an initial `Pull Request`_.


Licensing
---------

Finally, because we want to make the data part of the actual tests
that are run every time when new code is committed to the repository,
we would need the data to be made available under an `open license`_
(preferrable `CC0`_ (public domain) or `CC-BY`_ (attribution
required)). The dataset will carry the license and your authorship.

At the moment, all included data sets are in the public domain via CC0_.

.. _open license:
   https://opendefinition.org/licenses/#recommended-conformant-licenses
.. _CC0: https://creativecommons.org/publicdomain/zero/1.0/
.. _`CC-BY`: http://opendefinition.org/licenses/cc-by/


.. _process:

Process
-------

1. Raise an issue in the `alchemtest issue tracker`_ proposing the new
   data set. In this issue we will do all discussions.
2. Fork the alchemtest repo and create a branch for your dataset.
3. Add your dataset to your branch.  Follow the existing layout.
   
   * Choose a top level directory. If your data files are for GROMACS,
     add it to `alchemtest/gmx`_ or for NAMD to `alchemtest/namd`_,
     etc. If you support a new code, create a new directory.
   * Create a *subdirectory* for your dataset, choose a good, short name for
     the dataset and the directory.

     * Create one or more additional directories inside your dataset
       directory for your actual data files; do whatever seems natural
       for your problem.       
     * *Copy your data files to the appropriate
       subdirectories*. Consider compressing them with :program:`gzip`
       or :program:`bzip2` (alchemlyb can read compressed files).       
     * Check the :file:`MANIFEST.in`: make sure that the line

       .. code-block:: bash

          recursive-include src/alchemtest *.gz *.bz2 *.zip *.rst *.txt *.out *.xvg

       will include your files into the package: If your filename
       extension(s) are not matched, add them.
     * Create a `restructured text (reST)`_ file :file:`descr.rst`
       that describes the dataset. Look at other description files as
       examples: copy one that is close in what you need and
       modify. The description will show up in the online
       documentation and will be part of the dataset
       :class:`~alchemtest.Bunch`.
	      
   * Add an accessor function :func:`load_MYDATASET()` to the
     :file:`access.py` file at the top of the code directory. The
     accessor function makes the dataset available as a :class:`dict`
     under the *data* key in the :class:`~alchemtest.Bunch`. The data
     are typically another :class:`dict` with different parts of a
     calculation such as Coulomb and VDW parts being different keys in a
     dictionary. All files that are needed for a single free energy
     calculation are in a :class:`list` under the appropriate key.  The
     description text is added the *DESCR* key.

     Again, copy an existing function and modify.     
   * Add an ``from .access import load_MYDATASET`` to the
     top-level :file:`__init__.py` to make your accessor function
     part of alchemtest.     
4. Locally test that you can load your dataset::

     from alchemtest.MYCODE.MYDATASET import load_MYDATASET
     d = load_MYDATASET()
     print(d.DESCR)
     print(d.data)

   You should see your description and the full path to your datafiles
   (possibly inside another dictionary). It should be possible to work
   with your dataset as shown under :ref:`usage`.

   Try building the documentation with

   .. code-block:: bash

      python setup.py build_sphinx

   and look at the docs in :file:`build/sphinx/html/index.html`.

   Check that your documentation is visible. If not, it's possible
   that another page needs to be added to the docs — just move ahead
   with the next step and ask in the comments on your Pull Request and
   we will help.

5. Create a `Pull Request`_ with your new code and files.

6. Add a *test* that checks that your files can be found. Look in the
   :file:`src/alchemtest/tests` directory and follow the examples that
   are already there.
   We are also happy to help you with this step — just ask.
   
   You can run the tests locally with `pytest` and you will also see
   that the tests are run on your PR.

7. Engage in the code review — we might have questions, suggestions,
   and requests for revisions to ensure that your contribution fits
   into the library.
   
8. Once your PR is accepted it will be merged by a developer and your
   dataset is part of **alchemtest** — Congratulations!
   

.. _`alchemtest issue tracker`: https://github.com/alchemistry/alchemtest/issues   

.. _`Pull Request`:
   https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork

.. _`alchemtest/gmx`:   
   https://github.com/alchemistry/alchemtest/tree/master/src/alchemtest/gmx

.. _`alchemtest/namd`:
   https://github.com/alchemistry/alchemtest/tree/master/src/alchemtest/namd

.. _`restructured text (reST)`:
   https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
