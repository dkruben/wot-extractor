# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/tooltips/quests_builders.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/tooltips/quests_builders.py
from __future__ import absolute_import
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.tooltips import contexts
from gui.shared.tooltips import quests
from gui.shared.tooltips.builders import DataBuilder
__all__ = ('getTooltipBuilders', )

def getTooltipBuilders():
    return (
     DataBuilder(TOOLTIPS_CONSTANTS.QUESTS_PREVIEW, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, quests.QuestsPreviewTooltipData(contexts.QuestsBoosterContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.SHEDULE_QUEST, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, quests.ScheduleQuestTooltipData(contexts.QuestContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.MISSION_VEHICLE, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, quests.MissionVehiclesConditionTooltipData(contexts.QuestContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.MISSION_VEHICLE_TYPE, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, quests.MissionVehiclesTypeTooltipData(contexts.QuestContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.ADDITIONAL_AWARDS, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, quests.AdditionalAwardTooltipData(contexts.QuestContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.PACK_RENT_VEHICLES, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, quests.RentVehicleAwardTooltipData(contexts.QuestContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.UNAVAILABLE_QUEST, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, quests.UnavailableQuestTooltipData(contexts.QuestContext())))
