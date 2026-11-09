# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/Scaleform/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/Scaleform/__init__.py
from __future__ import absolute_import
from fun_random_common.fun_constants import ARENA_GUI_TYPE
from fun_random.gui.fun_gui_constants import FunRandomTooltipConstants
from gui.Scaleform.genConsts.FUNRANDOM_ALIASES import FUNRANDOM_ALIASES
from gui.Scaleform.daapi.settings import config as sf_config
from gui.shared.system_factory import registerScaleformLobbyPackages, registerLobbyTooltipsBuilders, registerScaleformBattlePackages, registerLifecycleHandledSubViews

def registerFunRandomScaleform():
    registerScaleformLobbyPackages(('fun_random.gui.Scaleform.daapi.view.lobby', ))
    registerScaleformBattlePackages(ARENA_GUI_TYPE.FUN_RANDOM, sf_config.BATTLE_PACKAGES + ('fun_random.gui.Scaleform.daapi.view.battle', ))
    registerLobbyTooltipsBuilders([
     (
      'fun_random.gui.Scaleform.daapi.view.tooltips.lobby_builders',
      FunRandomTooltipConstants.LOBBY_TOOLTIPS_SET)])
    registerLifecycleHandledSubViews([FUNRANDOM_ALIASES.FUN_RANDOM_HANGAR, FUNRANDOM_ALIASES.FUN_PROGRESSION])
