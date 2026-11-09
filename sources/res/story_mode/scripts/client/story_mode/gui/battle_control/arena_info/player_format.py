# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/battle_control/arena_info/player_format.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/battle_control/arena_info/player_format.py
from __future__ import absolute_import
from gui.battle_control.arena_info import player_format
from gui.battle_control.arena_info.player_format import PlayerFormatResult
from helpers import i18n

class StoryModeNameFormatter(player_format.PlayerFullNameFormatter):

    def format(self, vInfoVO, playerName=None):
        obj = super(StoryModeNameFormatter, self).format(vInfoVO, playerName)
        playerName = obj.playerName
        if playerName.startswith('#'):
            playerName = i18n.makeString(playerName)
        elif playerName.startswith(':'):
            playerName = obj.vehicleName
        return PlayerFormatResult(playerName, playerName, obj.playerFakeName, obj.clanAbbrev, obj.regionCode, obj.vehicleName)
