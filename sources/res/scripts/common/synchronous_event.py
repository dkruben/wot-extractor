# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/synchronous_event.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/synchronous_event.py
from __future__ import absolute_import
from wg_async import wg_async, forwardAsFuture, wg_await
from debug_utils import LOG_CURRENT_EXCEPTION
from Event import Event

class SynchronousEvent(Event):
    __slots__ = ()

    @wg_async
    def __call__(self, *args, **kwargs):
        for delegate in self[:]:
            try:
                yield wg_await(forwardAsFuture(delegate(*args, **kwargs)))
            except:
                LOG_CURRENT_EXCEPTION()
