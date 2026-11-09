# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/battle_control/controllers/equipment_triggers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/battle_control/controllers/equipment_triggers.py
from __future__ import absolute_import
from gui.battle_control.controllers.consumables.equipment_ctrl import _OrderItem, _ReplayOrderItem
from gui.Scaleform.genConsts.BATTLE_MARKERS_CONSTS import BATTLE_MARKERS_CONSTS

class _EventArtilleryItem(_OrderItem):

    def getMarker(self):
        return 'LSEventDeathZoneUI'

    def getMarkerColor(self):
        return BATTLE_MARKERS_CONSTS.COLOR_RED


class _ReplayEventArtilleryItem(_ReplayOrderItem):

    def getMarker(self):
        return 'LSEventDeathZoneUI'

    def getMarkerColor(self):
        return BATTLE_MARKERS_CONSTS.COLOR_RED
