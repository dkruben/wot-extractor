# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/events_containers/common/container_wrappers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/events_containers/common/container_wrappers.py
from __future__ import absolute_import
from functools import wraps
from constants import IS_DEVELOPMENT

def activateEventsContainer(withDebug=True, withCGF=True):

    def decorator(method):

        @wraps(method)
        def wrapper(*args, **kwargs):
            eventsContainer = method(*args, **kwargs)
            if IS_DEVELOPMENT and withDebug and kwargs.get('withDebug', True):
                eventsContainer.debugEvents()
            if withCGF:
                eventsContainer.attachCoreEvents()
            return eventsContainer

        return wrapper

    return decorator
