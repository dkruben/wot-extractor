# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/skeletons/gui/techtree_events.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/gui/techtree_events.py
from __future__ import absolute_import
from Event import Event

class ITechTreeEventsListener(object):
    onEventsUpdated = None
    onSettingsChanged = None

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError

    @property
    def actions(self):
        raise NotImplementedError

    def getUserName(self, actionID):
        raise NotImplementedError

    def getVehicles(self, nationID=None):
        raise NotImplementedError

    def setNationViewed(self, nationID):
        raise NotImplementedError

    def getNations(self, unviewed=False, actionID=None):
        raise NotImplementedError

    def getTimeTillEnd(self, actionID):
        raise NotImplementedError

    def getFinishTime(self, actionID):
        raise NotImplementedError

    def hasActiveAction(self, vehicleCD, nationID=None):
        raise NotImplementedError

    def getActiveAction(self, vehicleCD=None, nationID=None):
        raise NotImplementedError
