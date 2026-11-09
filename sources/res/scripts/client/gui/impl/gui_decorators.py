# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gui_decorators.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gui_decorators.py
from __future__ import absolute_import
import functools, inspect, logging
from frameworks.wulf import View, ViewStatus
from helpers.uniprof import regions
from py2to3.backport.inspect import getargspec
_REGION_FORMAT = 'view.{}.{}'
_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())

def args2params(*types):

    def _decorator(func):

        @functools.wraps(func)
        def _wrapper(*args):
            signature = getargspec(func).args
            if 'self' in signature:
                args, kwargs = (
                 args[0],), args[1]
                signature.remove('self')
            else:
                args, kwargs = tuple(), args[0]
            if types:
                for idx, name in enumerate(signature):
                    try:
                        kwargs[name] = types[idx](kwargs[name])
                    except (ValueError, TypeError) as e:
                        _logger.warning('There is an error while converting arg @%s[%s] to %s: %s', name, kwargs[name], str(types[idx]), str(e))

            return func(*args, **kwargs)

        return _wrapper

    return _decorator


def trackLifeCycle(uniqueName):
    return ViewLifeCycleToRegions(uniqueName)


class ViewLifeCycleToRegions(object):
    __slots__ = ('__uniqueName', '__viewStatus')

    def __init__(self, uniqueName):
        super(ViewLifeCycleToRegions, self).__init__()
        self.__uniqueName = uniqueName
        self.__viewStatus = ViewStatus.UNDEFINED

    def __call__(self, clazz):
        if View not in inspect.getmro(clazz):
            raise UserWarning(('The following argument {} is not subclass of View').format(clazz))

        def swap(func):

            @functools.wraps(func)
            def wrapper(view, oldStatus, newStatus, *args, **kwargs):
                func(view, oldStatus, newStatus, *args, **kwargs)
                self.__trigger(newStatus)

            return wrapper

        if not getattr(clazz, '__lifeCycleTracked__', False):
            setattr(clazz, '_swapStates', swap(getattr(clazz, '_swapStates')))
            setattr(clazz, '__lifeCycleTracked__', True)
        else:
            _logger.warning('Class already wrapped: %r', clazz)
        return clazz

    def __enter(self):
        regions.enterToRegion(_REGION_FORMAT.format(self.__uniqueName, ViewStatus.getKeyByValue(self.__viewStatus).lower()))

    def __exit(self):
        regions.exitFromRegion(_REGION_FORMAT.format(self.__uniqueName, ViewStatus.getKeyByValue(self.__viewStatus).lower()))

    def __trigger(self, newState):
        if self.__viewStatus != ViewStatus.UNDEFINED:
            self.__exit()
        self.__viewStatus = newState
        if self.__viewStatus != ViewStatus.DESTROYED:
            self.__enter()
