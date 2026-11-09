# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/tooltips/royale_battle_builders.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/tooltips/royale_battle_builders.py
from __future__ import absolute_import
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.app_loader import sf_battle
from gui.shared.gui_items import GUI_ITEM_TYPE
from battle_royale.gui.shared.tooltips.battle_royale_modules import BattleRoyaleModulesTooltip
from gui.shared.tooltips.builders import DataBuilder
from helpers import dependency
from items import parseIntCompactDescr
from skeletons.gui.battle_session import IBattleSessionProvider
__all__ = ('getTooltipBuilders', )

def getTooltipBuilders():
    return (
     DataBuilder(TOOLTIPS_CONSTANTS.BATTLE_ROYALE_MODULES, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, BattleRoyaleModulesTooltip(_BattleRoyaleBattleVehInfoContext())),)


class _BattleRoyaleBattleVehInfoContext(object):

    @sf_battle
    def app(self):
        return

    def buildItem(self, *args, **kwargs):
        intCD = args[0]
        itemTypeID, _, _ = parseIntCompactDescr(intCD)
        if itemTypeID == GUI_ITEM_TYPE.VEHICLE:
            vehicle = self.getVehicle()
            return (
             vehicle, vehicle)
        module = self.__getProgressionCtrl().getModule(intCD)
        currentModule = self.__getProgressionCtrl().getInstalledOnVehicleAnalogByIntCD(intCD)
        return (module, currentModule)

    def getVehicle(self):
        return self.__getProgressionCtrl().getInitialVehicle()

    @dependency.replace_none_kwargs(sessionProvider=IBattleSessionProvider)
    def __getProgressionCtrl(self, sessionProvider=None):
        return sessionProvider.dynamic.progression

    def getComponent(self):
        return
