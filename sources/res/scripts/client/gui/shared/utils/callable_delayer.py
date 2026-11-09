# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/utils/callable_delayer.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/utils/callable_delayer.py
from __future__ import absolute_import
import weakref, typing
from Event import Event
from WeakMethod import WeakMethodProxy
if typing.TYPE_CHECKING:
    from frameworks.wulf import View as WulfView
    from gui.Scaleform.framework.entities.View import View
    from _weakref import ReferenceType

class CallableDelayer(object):

    class _CleanupWrapper(object):

        def __init__(self, eventRef, wrappedFn, cleanupCallback):
            self.__eventRef = eventRef
            self.__wrappedFn = wrappedFn
            self.__cleanupCallback = cleanupCallback
            event = eventRef()
            if event is not None:
                event += self
            return

        def __del__(self):
            self.clear()

        def __call__(self):
            self.__wrappedFn()
            self.clear()

        def clear(self):
            event = self.__eventRef()
            if event is not None:
                event -= self
            self.__cleanupCallback(self)
            self.__wrappedFn = lambda : None
            return

    def __init__(self):
        self.__wrappers = []

    def __del__(self):
        self.clear()

    def delayUntilEvent(self, event, fn):
        self.__wrappers.append(self._CleanupWrapper(weakref.ref(event), fn, WeakMethodProxy(self.__removeWrapper)))

    def clear(self):
        for wrapper in self.__wrappers:
            wrapper.clear()

        self.__wrappers = []

    def __removeWrapper(self, wrapper):
        if wrapper in self.__wrappers:
            self.__wrappers.remove(wrapper)


def delayUntilParentWindowReady(delayer, view, fn):
    if view:
        window = view.getParentWindow()
        if window and window.isReady:
            fn()
        else:
            delayer.delayUntilEvent(window.onReady, fn)
    else:
        fn()
