# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/wrapped_reflection_framework.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/wrapped_reflection_framework.py
from __future__ import absolute_import
from constants import IS_UE_EDITOR
from collections import namedtuple
from contextlib import contextmanager
if IS_UE_EDITOR:
    from reflection_framework import ReflectionMetaclass
    from reflection_framework import reflectedNamedTuple
    from reflection_framework import notifyPropertiesReset
else:
    ReflectionMetaclass = type
    reflectedNamedTuple = namedtuple

    @contextmanager
    def notifyPropertiesReset(obj):
        yield
        return
