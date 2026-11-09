# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/client/comp7_light/gui/Scaleform/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/client/comp7_light/gui/Scaleform/__init__.py
from __future__ import absolute_import
from comp7_light.gui.Scaleform.genConsts.TOOLTIPS_BATTLE_CONSTANTS import TOOLTIPS_BATTLE_CONSTANTS as COMP7_LIGHT_BATTLE_TOOLTIPS
from comp7_light.gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as COMP7_LIGHT_TOOLTIPS
from comp7_light_constants import ARENA_GUI_TYPE
from gui.Scaleform.daapi.settings.config import BATTLE_PACKAGES
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.system_factory import registerScaleformLobbyPackages, registerLobbyTooltipsBuilders, registerScaleformBattlePackages, registerBattleTooltipsBuilders

def registerComp7LightScaleform():
    registerScaleformLobbyPackages(('comp7_light.gui.Scaleform.daapi.view.lobby', ))
    registerLobbyTooltipsBuilders([
     (
      'comp7_light.gui.Scaleform.daapi.view.tooltips.comp7_light_lobby_builders',
      COMP7_LIGHT_TOOLTIPS.COMP7_LIGHT_LOBBY_SET)])
    registerScaleformBattlePackages(ARENA_GUI_TYPE.COMP7_LIGHT, BATTLE_PACKAGES + ('comp7_light.gui.Scaleform.daapi.view.battle', ))
    COMP7_LIGHT_BATTLE_TOOLTIPS.COMP7_LIGHT_BATTLE_SET.append(TOOLTIPS_CONSTANTS.VEHICLE_ROLES)
    registerBattleTooltipsBuilders([
     (
      'comp7_light.gui.Scaleform.daapi.view.tooltips.comp7_light_battle_builders',
      COMP7_LIGHT_BATTLE_TOOLTIPS.COMP7_LIGHT_BATTLE_SET)])
