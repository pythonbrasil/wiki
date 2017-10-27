`Replacer <https://github.com/narusemotoki/replacer>`_
======================================================

This is plugin of Pelican. You can replace a text of a generated HTML. You can write replacing rule in your pelicanconf.py.

Example
=======

This example is replacing from '<table border="1" class="docutils">' to '<table class="table table-striped table-bordered table-hover">'.

::

    REPLACES = (
        (u'<table border="1" class="docutils">', u'<table class="table table-striped table-bordered table-hover">'),
    )
