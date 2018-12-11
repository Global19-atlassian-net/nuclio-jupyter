#!/usr/bin/env ipython

from contextlib import redirect_stdout
from io import StringIO
from os import path

from IPython import get_ipython

from nuclio.magic import commands

help_template = '''\
{name}
{underline}

::

   In [1]: %nuclio help {name}
   {help}
'''

file_header = '''\
.. Automatically generated by {}, do not edit manually

%nuclio magic
=============

When you import the `nuclio` module, a new ``%nuclio`` magic command will be
added to IPython/Jupyter.

'''.format(path.basename(__file__))


def magic_help(kernel, name):
    io = StringIO()
    with redirect_stdout(io):
        kernel.run_cell('%nuclio help {}'.format(name))

    if not name:
        name = 'Overview'
    underline = '-' * len(name)
    help = io.getvalue().strip()
    return help_template.format(name=name, underline=underline, help=help)


if __name__ == '__main__':
    kernel = get_ipython()
    if kernel is None:
        raise SystemExit('error: not running under IPython/Jupyter')

    print(file_header)
    for cmd in [''] + sorted(commands):
        print(magic_help(kernel, cmd))