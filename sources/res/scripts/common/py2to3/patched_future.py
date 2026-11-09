# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/py2to3/patched_future.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/py2to3/patched_future.py
from __future__ import absolute_import
from typing import TYPE_CHECKING
if TYPE_CHECKING:

    def with_metaclass(meta, *bases):
        return meta('temporary_class', bases, {})


else:
    from future.utils import with_metaclass
