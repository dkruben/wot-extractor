# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/Scaleform/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/Scaleform/__init__.py
from __future__ import absolute_import
from frontline.constants.aliases import FrontlineHangarAliases
from gui.shared.system_factory import registerBattleTooltipsBuilders, registerLobbyTooltipsBuilders, registerLifecycleHandledSubViews
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as _TOOLTIPS

def registerFLScaleform():
    registerBattleTooltipsBuilders([
     (
      'frontline.gui.Scaleform.daapi.view.tooltips.frontline_battle_builders', _TOOLTIPS.FRONTLINE_BATTLE_SET)])
    registerLobbyTooltipsBuilders([
     (
      'frontline.gui.Scaleform.daapi.view.tooltips.frontline_lobby_builders', _TOOLTIPS.FRONTLINE_LOBBY_SET)])
    registerLifecycleHandledSubViews([FrontlineHangarAliases.FRONTLINE_LOBBY_HANGAR])
