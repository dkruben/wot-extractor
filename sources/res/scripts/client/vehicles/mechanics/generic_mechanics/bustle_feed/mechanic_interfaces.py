# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicles/mechanics/generic_mechanics/bustle_feed/mechanic_interfaces.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicles/mechanics/generic_mechanics/bustle_feed/mechanic_interfaces.py
from __future__ import absolute_import

class IBustleFeedEventsLogic(object):
    onReloadTriggered = None

    def processReloadTriggered(self, shell, side, duration):
        raise NotImplementedError


class IBustleFeedListenerLogic(object):

    def onReloadTriggered(self, shell, side, duration):
        pass
