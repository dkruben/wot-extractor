# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/Scaleform/daapi/view/lobby/hangar/header_helpers/quest_flags_getters.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/Scaleform/daapi/view/lobby/hangar/header_helpers/quest_flags_getters.py
from __future__ import absolute_import
from comp7.gui.Scaleform.daapi.view.lobby.hangar.header_helpers.flag_constants import QuestFlagTypes
from gui.Scaleform.daapi.view.lobby.hangar.header_helpers.quest_flags_getters import BaseQuestFlagsGetter

class Comp7QuestFlagsGetter(BaseQuestFlagsGetter):
    _SUPPORTED_FLAGS = (
     QuestFlagTypes.COMP7, QuestFlagTypes.MARATHON)


class Comp7TournamentQuestFlagsGetter(BaseQuestFlagsGetter):
    _SUPPORTED_FLAGS = (
     QuestFlagTypes.PERSONAL_MISSIONS, QuestFlagTypes.BATTLE, QuestFlagTypes.MARATHON, QuestFlagTypes.ELEN)
