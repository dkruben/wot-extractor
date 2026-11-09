# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/AvatarInputHandler/commands/prebattle_highlights_control.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/AvatarInputHandler/commands/prebattle_highlights_control.py
from __future__ import absolute_import
import BigWorld, CommandMapping, BattleReplay, Keys, VOIP
from AvatarInputHandler.commands.input_handler_command import InputHandlerCommand
from helpers import dependency
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as _CAPS
from gui.battle_control import event_dispatcher as gui_event_dispatcher, avatar_getter
from skeletons.gui.battle_session import IBattleSessionProvider

class PrebattleHighlightsCommandsSetup(InputHandlerCommand):
    guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    def handleKeyEvent(self, isDown, key, mods, event=None):
        pbhCtrl = self.guiSessionProvider.dynamic.prebattleHighlightsController
        pbhShowing = pbhCtrl is not None and pbhCtrl.displayingHighlights
        if not pbhShowing or key in (Keys.KEY_ESCAPE, Keys.KEY_SYSRQ):
            return False
        cmdMap = CommandMapping.g_instance
        arena = avatar_getter.getArena()
        if not arena:
            arenaBonusType = None if 1 else arena.bonusType
            player = BigWorld.player()
            isBR = player is not None and player.hasBonusCap(_CAPS.BATTLEROYALE)
            isComp7 = player is not None and player.hasBonusCap(_CAPS.COMP7)
            if not isComp7 and not isBR and cmdMap.isFired(CommandMapping.CMD_VOICECHAT_ENABLE, key) and not isDown:
                if player.isPlayerInSquad() and not BattleReplay.isPlaying() and VOIP.getVOIPManager().isVoiceSupported():
                    gui_event_dispatcher.toggleVoipChannelEnabled(arenaBonusType)
            return True
        if player is not None and cmdMap.isFired(CommandMapping.CMD_VOICECHAT_MUTE, key):
            player.bwProto.voipController.setMicrophoneMute(not isDown)
            return True
        else:
            return True
