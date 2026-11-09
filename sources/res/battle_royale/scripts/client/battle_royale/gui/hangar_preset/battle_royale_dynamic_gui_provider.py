# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/hangar_preset/battle_royale_dynamic_gui_provider.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/hangar_preset/battle_royale_dynamic_gui_provider.py
from __future__ import absolute_import
from constants import QUEUE_TYPE, ARENA_BONUS_TYPE
from gui.hangar_presets.providers import DefaultHangarDynamicGuiProvider
from helpers import dependency
from skeletons.gui.game_control import IPlatoonController
from battle_royale.gui.Scaleform.daapi.view.lobby.header.helpers.controls_helpers import BattleRoyaleLobbyHeaderHelper

class BattleRoyaleHangarDynamicGuiProvider(DefaultHangarDynamicGuiProvider):
    __slots__ = ()
    _QUEUE_TYPE = QUEUE_TYPE.BATTLE_ROYALE
    _BONUS_TYPES = (ARENA_BONUS_TYPE.BATTLE_ROYALE_SOLO, ARENA_BONUS_TYPE.BATTLE_ROYALE_SQUAD)
    _LOBBY_HEADER_HELPER = BattleRoyaleLobbyHeaderHelper
    _platoonCtrl = dependency.descriptor(IPlatoonController)

    def getSuggestedBonusType(self):
        if self._platoonCtrl.isInPlatoon():
            return ARENA_BONUS_TYPE.BATTLE_ROYALE_SQUAD
        return ARENA_BONUS_TYPE.BATTLE_ROYALE_SOLO
