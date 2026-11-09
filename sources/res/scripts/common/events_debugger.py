# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/events_debugger.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/events_debugger.py
from __future__ import absolute_import
from debug_utils import LOG_DEBUG_DEV

def _iterEventNames(events):
    return (name for name in dir(events) if name.startswith('on'))


class EventsDebugger(object):

    def __init__(self, events):
        for eventName in self._iterEventNames(events):
            event = getattr(events, eventName)
            processor = getattr(self, eventName)
            event += processor

    def _getDebugPrefix(self):
        return '[EVENT]'

    def _buildDebugString(self, item):
        return '%s %s' % (self._getDebugPrefix(), item)

    def _iterEventNames(self, events):
        return (eventName for eventName in _iterEventNames(events) if self._shouldHandle(eventName))

    def _shouldHandle(self, eventName):
        return True

    def __getattr__(self, item):
        return (lambda *args, **kwargs: LOG_DEBUG_DEV(self._buildDebugString(item), *args, **kwargs))
