# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/distutils/tests/setuptools_extension.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/distutils/tests/setuptools_extension.py
from distutils.core import Extension as _Extension
from distutils.core import Distribution as _Distribution

def _get_unpatched(cls):
    while cls.__module__.startswith('setuptools'):
        cls, = cls.__bases__

    if not cls.__module__.startswith('distutils'):
        raise AssertionError('distutils has already been patched by %r' % cls)
    return cls


_Distribution = _get_unpatched(_Distribution)
_Extension = _get_unpatched(_Extension)
try:
    from Pyrex.Distutils.build_ext import build_ext
except ImportError:
    have_pyrex = False
else:
    have_pyrex = True

class Extension(_Extension):
    if not have_pyrex:

        def __init__(self, *args, **kw):
            _Extension.__init__(self, *args, **kw)
            sources = []
            for s in self.sources:
                if s.endswith('.pyx'):
                    sources.append(s[:-3] + 'c')
                else:
                    sources.append(s)

            self.sources = sources


class Library(Extension):
    pass


import sys, distutils.core, distutils.extension
distutils.core.Extension = Extension
distutils.extension.Extension = Extension
if 'distutils.command.build_ext' in sys.modules:
    sys.modules['distutils.command.build_ext'].Extension = Extension
