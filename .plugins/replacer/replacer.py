# -*- coding: utf-8 -*-
import pelican
import sys

python3 = sys.version_info >= (3, 0, 0)


def init(pelican_object):
    # I have no good idea. Pass settings to replace function.
    global replaces
    replaces = pelican_object.settings.get('REPLACES', ())


def replace(path, context):
    with open(path, 'r') as f:
        s = f.read()
        for src, tgt in replaces:
            if python3:
                s = s.replace(src, tgt)
            else:
                if type(s) is str:
                    s = s.decode('utf-8').replace(src.decode('utf-8'), tgt.decode('utf-8'))
                else:
                    s = s.replace(src, tgt)

    with open(path, 'w') as f:
        if python3:
            f.write(s)
        else:
            f.write(s.encode('utf-8'))


def register():
    pelican.signals.initialized.connect(init)
    pelican.signals.content_written.connect(replace)
