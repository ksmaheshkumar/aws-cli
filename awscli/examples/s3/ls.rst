The following ``ls`` command lists all of the bucket owned by the user.  In this example, the user owns the buckets
``mybucket`` and ``mybucket2``.  The ``CreationTime`` is the date the bucket was created.  Note if ``s3://`` is used for
the path argument ``<S3Path>``, it will list all of the buckets as well::

    aws s3 ls

Output::

    2013-07-11 17:08:50 mybucket
    2013-07-24 14:55:44 mybucket2

The following ``ls`` command lists objects and common prefixes under a spcified bucket and prefix.  In this example, the
user owns the bucket ``mybucket`` with the objects ``test.txt`` and ``somePrefix/test.txt``.  The ``LastWriteTime`` and
``Length`` are arbitrary::

    aws s3 ls s3://mybucket

Output::

                               PRE somePrefix/
    2013-07-25 17:06:27         88 test.txt


The following ``ls`` command lists objects and common prefixes under a specified bucket and prefix.  However, there are
no objects nor common prefixes under the specified bucket and prefix::

    aws s3 ls s3://mybucket/noExistPrefix

Output::

    None

The following ``ls`` command will recursively list objects in a bucket.  Rather than showing ``PRE dirname/`` in the
output, all the content in a bucket will be listed in order::

    aws s3 ls s3://mybucket --recursive

Output::

    2013-09-02 21:37:53         10 a.txt
    2013-09-02 21:37:53    2863288 foo.zip
    2013-09-02 21:32:57         23 foo/bar/.baz/a
    2013-09-02 21:32:58         41 foo/bar/.baz/b
    2013-09-02 21:32:57        281 foo/bar/.baz/c
    2013-09-02 21:32:57         73 foo/bar/.baz/d
    2013-09-02 21:32:57        452 foo/bar/.baz/e
    2013-09-02 21:32:57        896 foo/bar/.baz/hooks/bar
    2013-09-02 21:32:57        189 foo/bar/.baz/hooks/foo
    2013-09-02 21:32:57        398 z.txt

The following ``ls`` command demonstrates the same command using the --human-readable
and --summarize options. --human-readable displays file size in
Bytes/MiB/KiB/GiB/TiB/PiB/EiB. --summarize displays the total number of objects
and total size at the end of the result listing::

    aws s3 ls s3://mybucket --recursive --human-readable --summarize

Output::

    2013-09-02 21:37:53   10 Bytes a.txt
    2013-09-02 21:37:53  2.9 MiB foo.zip
    2013-09-02 21:32:57   23 Bytes foo/bar/.baz/a
    2013-09-02 21:32:58   41 Bytes foo/bar/.baz/b
    2013-09-02 21:32:57  281 Bytes foo/bar/.baz/c
    2013-09-02 21:32:57   73 Bytes foo/bar/.baz/d
    2013-09-02 21:32:57  452 Bytes foo/bar/.baz/e
    2013-09-02 21:32:57  896 Bytes foo/bar/.baz/hooks/bar
    2013-09-02 21:32:57  189 Bytes foo/bar/.baz/hooks/foo
    2013-09-02 21:32:57  398 Bytes z.txt

    Total Objects: 10
       Total Size: 2.9 MiB
