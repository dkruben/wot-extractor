# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/lobby/tank_setup/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/scaleform/daapi/view/lobby/tank_setup/__init__.py
from __future__ import absolute_import
from halloween.gui.scaleform.genConsts.HALLOWEEN_CM_HANDLER_TYPE import HALLOWEEN_CM_HANDLER_TYPE
from halloween.gui.scaleform.daapi.view.lobby.tank_setup.context_menu.consumable import HWHangarConsumableSlotContextMenu

def getContextMenuHandlers():
    return (
     (
      HALLOWEEN_CM_HANDLER_TYPE.TANK_SETUP_HW_HANGAR_CONSUMABLE_SLOT, HWHangarConsumableSlotContextMenu),)


def getViewSettings():
    return ()


def getBusinessHandlers():
    return ()
