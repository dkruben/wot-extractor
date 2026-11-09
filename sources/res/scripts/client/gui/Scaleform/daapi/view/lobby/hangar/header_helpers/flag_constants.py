# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/hangar/header_helpers/flag_constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/header_helpers/flag_constants.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.lobby.hangar.header_helpers.personal_mission_flags import PersonalMissionsFlag
from gui.Scaleform.daapi.view.lobby.hangar.header_helpers.quest_flags import RankedQuestsFlag, ElenQuestsFlag, BattleQuestsFlag, MarathonQuestsFlag, MapboxQuestsFlag
from gui.shared.system_factory import registerQuestFlag

class QuestFlagTypes(object):
    PERSONAL_MISSIONS = 'personalMissions'
    BATTLE = 'battleQuests'
    MAPBOX = 'mapboxQuests'
    MARATHON = 'marathonQuests'
    ELEN = 'elenQuests'
    RANKED = 'rankedQuests'


registerQuestFlag(QuestFlagTypes.PERSONAL_MISSIONS, PersonalMissionsFlag)
registerQuestFlag(QuestFlagTypes.MARATHON, MarathonQuestsFlag)
registerQuestFlag(QuestFlagTypes.ELEN, ElenQuestsFlag)
registerQuestFlag(QuestFlagTypes.BATTLE, BattleQuestsFlag)
registerQuestFlag(QuestFlagTypes.RANKED, RankedQuestsFlag)
registerQuestFlag(QuestFlagTypes.MAPBOX, MapboxQuestsFlag)
