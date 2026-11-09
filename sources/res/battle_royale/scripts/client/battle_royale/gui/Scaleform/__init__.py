# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/Scaleform/__init__.py
from __future__ import absolute_import
from gui.Scaleform.genConsts.BATTLEROYALE_ALIASES import BATTLEROYALE_ALIASES
from gui.shared.system_factory import registerScaleformBattlePackages, registerScaleformLobbyPackages, registerBattleTooltipsBuilders, registerLobbyTooltipsBuilders, registerHangarDynamicGuiProvider, registerLifecycleHandledSubViews
from constants import ARENA_GUI_TYPE, QUEUE_TYPE
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as _TOOLTIPS
from gui.Scaleform.required_libraries_config import addBattleRequiredLibraries
from battle_royale.gui.hangar_preset.battle_royale_dynamic_gui_provider import BattleRoyaleHangarDynamicGuiProvider

def registerBRBattlePackages():
    registerScaleformBattlePackages(ARENA_GUI_TYPE.BATTLE_ROYALE, ('battle_royale.gui.Scaleform.daapi.view.battle',
                                                                   'battle_royale.gui.Scaleform.daapi.view.battle.shared',
                                                                   'messenger.gui.Scaleform.view.battle',
                                                                   'gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics',
                                                                   'gui.impl.battle.random',
                                                                   'gui.impl.battle.shared'))


def registerBRLobbyPackages():
    registerScaleformLobbyPackages([
     'battle_royale.gui.Scaleform.daapi.view.lobby',
     'battle_royale.gui.impl.lobby.views'])


def registerBRTooltipsBuilders():
    registerBattleTooltipsBuilders([
     (
      'battle_royale.gui.Scaleform.daapi.view.tooltips.royale_battle_builders', _TOOLTIPS.ROYALE_BATTLE_SET)])
    registerLobbyTooltipsBuilders([
     (
      'battle_royale.gui.Scaleform.daapi.view.tooltips.royale_lobby_builders', _TOOLTIPS.ROYALE_LOBBY_SET),
     (
      'battle_royale.gui.Scaleform.daapi.view.tooltips.royale_battle_builders', _TOOLTIPS.ROYALE_BATTLE_SET)])
    registerLifecycleHandledSubViews([BATTLEROYALE_ALIASES.BR_HANGAR_VIEW])


def registerCustomSwf():
    addBattleRequiredLibraries(['ub_components.swf'], ARENA_GUI_TYPE.BATTLE_ROYALE, 'BattleRoyalePersonality')


def registerBRBattleQueueProvider():
    from gui.prb_control import prb_utils
    from battle_royale.gui.Scaleform.daapi.view.lobby.battle_queue_provider import BattleRoyaleQueueProvider
    prb_utils.addProviderBattleQueueCls(QUEUE_TYPE.BATTLE_ROYALE, BattleRoyaleQueueProvider, 'BattleRoyalePersonality')


def registerBRHangarPresetGetter():
    registerHangarDynamicGuiProvider(QUEUE_TYPE.BATTLE_ROYALE, BattleRoyaleHangarDynamicGuiProvider)
