# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/feature/util/fun_wrappers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/feature/util/fun_wrappers.py
from __future__ import absolute_import
from functools import wraps
import operator

def ifNotificationsEnabled(method):

    @wraps(method)
    def wrapper(notifications, *args, **kwargs):
        if notifications.isNotificationsEnabled():
            method(notifications, *args, **kwargs)

    return wrapper


def ifNotificationsAllowed(useQueue=True):

    def decorator(method):

        @wraps(method)
        def wrapper(notifications, notification):
            if notifications.isNotificationsAllowed():
                method(notifications, notification)
            elif useQueue:
                notifications.addToQueue(notification)

        return wrapper

    return decorator


def hasActiveProgression(defReturn=None, abortAction=None):

    def decorator(method):

        @wraps(method)
        def wrapper(progressionWatcher, *args, **kwargs):
            if progressionWatcher.getActiveProgression() is not None:
                return method(progressionWatcher, *args, **kwargs)
            else:
                if abortAction is not None:
                    return operator.methodcaller(abortAction)(progressionWatcher)
                return defReturn

        return wrapper

    return decorator


def hasAnySubMode(defReturn=None, abortAction=None):

    def decorator(method):

        @wraps(method)
        def wrapper(subModesWatcher, *args, **kwargs):
            if subModesWatcher.getSubModes():
                return method(subModesWatcher, *args, **kwargs)
            else:
                if abortAction is not None:
                    return operator.methodcaller(abortAction)(subModesWatcher)
                return defReturn

        return wrapper

    return decorator


def hasBattleSubMode(defReturn=None, abortAction=None):

    def decorator(method):

        @wraps(method)
        def wrapper(subModesWatcher, *args, **kwargs):
            if subModesWatcher.getBattleSubMode() is not None:
                return method(subModesWatcher, *args, **kwargs)
            else:
                if abortAction is not None:
                    return operator.methodcaller(abortAction)(subModesWatcher)
                return defReturn

        return wrapper

    return decorator


def hasDesiredSubMode(defReturn=None, abortAction=None):

    def decorator(method):

        @wraps(method)
        def wrapper(subModesWatcher, *args, **kwargs):
            if subModesWatcher.getDesiredSubMode() is not None:
                return method(subModesWatcher, *args, **kwargs)
            else:
                if abortAction is not None:
                    return operator.methodcaller(abortAction)(subModesWatcher)
                return defReturn

        return wrapper

    return decorator


def hasHoldingSubMode(defReturn=None, abortAction=None):

    def decorator(method):

        @wraps(method)
        def wrapper(subModesHolder, *args, **kwargs):
            if subModesHolder.getHoldingSubMode() is not None:
                return method(subModesHolder, *args, **kwargs)
            else:
                if abortAction is not None:
                    return operator.methodcaller(abortAction)(subModesHolder)
                return defReturn

        return wrapper

    return decorator


def hasMultipleSubModes(defReturn=None, abortAction=None):

    def decorator(method):

        @wraps(method)
        def wrapper(subModesWatcher, *args, **kwargs):
            if len(subModesWatcher.getSubModes()) > 1:
                return method(subModesWatcher, *args, **kwargs)
            else:
                if abortAction is not None:
                    return operator.methodcaller(abortAction)(subModesWatcher)
                return defReturn

        return wrapper

    return decorator


def hasSingleSubMode(defReturn=None, abortAction=None):

    def decorator(method):

        @wraps(method)
        def wrapper(subModesWatcher, *args, **kwargs):
            if len(subModesWatcher.getSubModes()) == 1:
                return method(subModesWatcher, *args, **kwargs)
            else:
                if abortAction is not None:
                    return operator.methodcaller(abortAction)(subModesWatcher)
                return defReturn

        return wrapper

    return decorator


def hasSpecifiedSubMode(defReturn=None, abortAction=None):

    def decorator(method):

        @wraps(method)
        def wrapper(subModesWatcher, subModeID, *args, **kwargs):
            if subModesWatcher.getSubMode(subModeID) is not None:
                return method(subModesWatcher, subModeID, *args, **kwargs)
            else:
                if abortAction is not None:
                    return operator.methodcaller(abortAction)(subModesWatcher)
                return defReturn

        return wrapper

    return decorator


def hasSpecifiedSubModes(defReturn=None, abortAction=None):

    def decorator(method):

        @wraps(method)
        def wrapper(subModesWatcher, subModesIDs, *args, **kwargs):
            subModes = subModesWatcher.getSubModes(subModesIDs=subModesIDs)
            if len(subModesIDs) == len(subModes):
                return method(subModesWatcher, subModesIDs, *args, **kwargs)
            else:
                if abortAction is not None:
                    return operator.methodcaller(abortAction)(subModesWatcher)
                return defReturn

        return wrapper

    return decorator


def avoidSubModesStates(states=(), defReturn=None, abortAction=None):

    def decorator(method):

        @wraps(method)
        def wrapper(subModesWatcher, *args, **kwargs):
            status = subModesWatcher.getSubModesStatus()
            if status.state not in states:
                return method(subModesWatcher, status, *args, **kwargs)
            else:
                if abortAction is not None:
                    return operator.methodcaller(abortAction)(subModesWatcher)
                return defReturn

        return wrapper

    return decorator


def filterHoldingSubModeUpdates(method):

    @wraps(method)
    def wrapper(subModesHolder, event, *args, **kwargs):
        if subModesHolder.getHoldingSubMode().getSubModeID() in event.subModes:
            method(subModesHolder, event, *args, **kwargs)

    return wrapper


def skipNoSubModesAction(method):

    @wraps(method)
    def wrapper(controller, subModesToAction, *args, **kwargs):
        if subModesToAction:
            return method(controller, subModesToAction, *args, **kwargs)
        return subModesToAction

    return wrapper
