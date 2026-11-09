# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/helpers/uniprof/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/uniprof/__init__.py
from __future__ import absolute_import
import BigWorld
__all__ = ('regionDecorator', 'enterToRegion', 'exitFromRegion')

def _isRegionSupported():
    if not hasattr(BigWorld, 'uniprofRegionEnter'):
        return False
    if not hasattr(BigWorld, 'uniprofRegionExit'):
        return False
    return True


_IS_REGION_SUPPORTED = _isRegionSupported()
if _IS_REGION_SUPPORTED:
    from .regions import regionDecorator
    from .regions import enterToRegion, exitFromRegion
else:

    class _DummyDecorator(object):
        __slots__ = ()

        def __call__(self, func):
            return func


    def enterToRegion(*_):
        pass


    def exitFromRegion(*_):
        pass


    def regionDecorator(*_, **__):
        return _DummyDecorator()
