# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/Scaleform/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/Scaleform/__init__.py
from __future__ import absolute_import
from comp7.gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as COMP7_TOOLTIPS
from comp7_common.comp7_constants import ARENA_GUI_TYPE
from comp7.gui.Scaleform.genConsts.TOOLTIPS_BATTLE_CONSTANTS import TOOLTIPS_BATTLE_CONSTANTS as COMP7_BATTLE_TOOLTIPS
from gui.Scaleform.daapi.settings.config import BATTLE_PACKAGES
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.system_factory import registerScaleformLobbyPackages, registerLobbyTooltipsBuilders, registerScaleformBattlePackages, registerBattleTooltipsBuilders

def registerComp7Scaleform():
    registerScaleformLobbyPackages(('comp7.gui.Scaleform.daapi.view.lobby', ))
    registerScaleformBattlePackages(ARENA_GUI_TYPE.COMP7, BATTLE_PACKAGES + ('comp7.gui.Scaleform.daapi.view.battle', ))
    registerScaleformBattlePackages(ARENA_GUI_TYPE.TOURNAMENT_COMP7, BATTLE_PACKAGES + ('comp7.gui.Scaleform.daapi.view.battle', ))
    registerScaleformBattlePackages(ARENA_GUI_TYPE.TRAINING_COMP7, BATTLE_PACKAGES + ('comp7.gui.Scaleform.daapi.view.battle', ))
    registerLobbyTooltipsBuilders([
     (
      'comp7.gui.Scaleform.daapi.view.tooltips.comp7_lobby_builders', COMP7_TOOLTIPS.COMP7_LOBBY_SET)])
    COMP7_BATTLE_TOOLTIPS.COMP7_BATTLE_SET.append(TOOLTIPS_CONSTANTS.VEHICLE_ROLES)
    registerBattleTooltipsBuilders([
     (
      'comp7.gui.Scaleform.daapi.view.tooltips.comp7_battle_builders', COMP7_BATTLE_TOOLTIPS.COMP7_BATTLE_SET)])
