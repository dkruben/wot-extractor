# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/veh_mechanics/battle/updaters/updaters_common.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/veh_mechanics/battle/updaters/updaters_common.py
from __future__ import absolute_import
import typing, weakref
from events_containers.common.containers import ClientEventsContainer

class IViewUpdater(object):

    def initialize(self):
        pass

    def finalize(self):
        pass

    def destroy(self):
        pass


class ViewUpdatersCollection(object):

    def __init__(self):
        self.__updaters = []

    def initialize(self, updaters):
        self.__updaters = updaters
        for updater in self.__updaters:
            updater.initialize()

    def finalize(self):
        for updater in self.__updaters:
            updater.finalize()

    def destroy(self):
        updaters, self.__updaters = self.__updaters, []
        for updater in updaters:
            updater.destroy()


class ViewUpdater(ClientEventsContainer, IViewUpdater):

    def __init__(self, view):
        super(ViewUpdater, self).__init__()
        self.__view = weakref.proxy(view)

    @property
    def view(self):
        return self.__view

    def destroy(self):
        self.__view = None
        super(ViewUpdater, self).destroy()
        return
