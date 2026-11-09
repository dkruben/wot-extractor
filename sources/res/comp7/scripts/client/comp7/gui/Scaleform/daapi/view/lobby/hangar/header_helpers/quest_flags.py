# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/Scaleform/daapi/view/lobby/hangar/header_helpers/quest_flags.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/Scaleform/daapi/view/lobby/hangar/header_helpers/quest_flags.py
from __future__ import absolute_import
import constants
from gui.Scaleform.daapi.view.lobby.hangar.header_helpers.quest_flags import BattleQuestsFlag
from helpers import dependency
from skeletons.gui.game_control import IComp7Controller

class Comp7QuestsFlag(BattleQuestsFlag):
    __slots__ = ()
    __comp7Controller = dependency.descriptor(IComp7Controller)

    @classmethod
    def _getQuests(cls, vehicle):
        quests = super(cls, Comp7QuestsFlag)._getQuests(vehicle)
        return [quest for quest in quests if quest.hasBonusType(constants.ARENA_BONUS_TYPE.COMP7)]
