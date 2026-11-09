# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/helpers/rest_bonus.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/rest_bonus.py
from __future__ import absolute_import
import typing
from gui.game_control.rest_bonus_controller import REST_BONUS_BASE_FACTOR, REST_BONUS_XP_FACTOR_BONUS
if typing.TYPE_CHECKING:
    from typing import Dict, List, Tuple
    from gui.server_events.event_items import Quest

def getRestBonusData(questsProgress, restBonusQuests):
    factor = 0.0
    questIDs = []
    for questID in questsProgress:
        quest = restBonusQuests.get(questID)
        if quest is None:
            continue
        for bonus in quest.getBonuses(REST_BONUS_XP_FACTOR_BONUS):
            factor += bonus.getValue() - REST_BONUS_BASE_FACTOR

        questIDs.append(questID)

    return (
     factor, questIDs)
