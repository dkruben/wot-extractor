# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/lobby/quest_packers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/gui/impl/lobby/quest_packers.py
from __future__ import absolute_import
from fort_rush.gui.impl.lobby.bonus_packers import getFortRushMissionBonusPacker
from fort_rush.gui.impl.lobby.bonus_packers import FortRushTokenBonusUIPacker
from gui.shared.missions.packers.events import DailyQuestUIDataPacker, findFirstConditionModel

class FortRushDailyQuestUIDataPacker(DailyQuestUIDataPacker):

    def _getBonusPacker(self):
        packer = getFortRushMissionBonusPacker()
        return packer

    def _resolveQuestIcon(self, model):
        conditionModel = findFirstConditionModel(model.postBattleCondition)
        if conditionModel is None:
            conditionModel = findFirstConditionModel(model.bonusCondition)
            if conditionModel is None:
                return
        model.setIcon(conditionModel.getIconKey())
        return
