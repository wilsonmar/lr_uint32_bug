lr_uint32_bug
=============

A Python script that fixes corrupted LoadRunner results.

Your results file is a good candidate for fixing if you see errors like:

    Internal error: <The given key was not present in the dictionary.> while inserting transaction event.

Usage
-----

To fix the results in the folder c:\result\file\location, run:

    lr_uint32_bug.py c:\result\file\location

License
-------

This script is licensed under the Apache license - see LICENSE.TXT
