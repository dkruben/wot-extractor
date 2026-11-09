# wot-extractor: codigo DESCOMPILADO de sources/res/server_side_replay/scripts/client/server_side_replay/gui/impl/lobby/filter/state.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: server_side_replay/scripts/client/server_side_replay/gui/impl/lobby/filter/state.py
from __future__ import absolute_import
from collections import defaultdict
from future.utils import viewitems
from past.builtins import basestring, unicode
from py2to3.moves.collections.abc import Iterable
from Event import Event
from server_side_replay.gui.impl.gen.view_models.views.lobby.filter_toggle_group_model import ToggleGroupType

class FilterState(object):
    GROUPS = ToggleGroupType

    def __init__(self, initialState=None):
        self.onStateChanged = Event()
        self._state = defaultdict(set)
        self.__searchString = u''
        self._initialState = initialState or {}
        self.isPrimeTime = False
        self.lastDays = 14
        self.reinit()

    def __contains__(self, item):
        return item in self._state

    def __getitem__(self, item):
        return self._state[item]

    def __iter__(self):
        return iter(self._state)

    @property
    def searchString(self):
        return self.__searchString

    @searchString.setter
    def searchString(self, value):
        self.__searchString = unicode(value)
        self.onStateChanged()

    @property
    def state(self):
        return self._state

    def clear(self):
        self.__clear()
        self.onStateChanged()

    def update(self, groupID, fieldID):
        if fieldID in self._state[groupID]:
            self._state[groupID].remove(fieldID)
        else:
            self._state[groupID].add(fieldID)
        self.onStateChanged()

    def reinit(self, state=None):
        self.__clear()
        self._reinitState(initialState=state)
        self.onStateChanged()

    def _reinitState(self, initialState=None):
        if initialState is not None:
            self._initialState = initialState
        if not self._initialState:
            return
        else:
            for groupID, value in viewitems(self._initialState):
                if isinstance(value, Iterable) and not isinstance(value, basestring):
                    for item in value:
                        self._state[groupID].add(item)

                else:
                    self._state[groupID].add(value)

            return

    def __clear(self):
        self._state = defaultdict(set)
        self.__searchString = u''
        self.isPrimeTime = False
        self.lastDays = 14
