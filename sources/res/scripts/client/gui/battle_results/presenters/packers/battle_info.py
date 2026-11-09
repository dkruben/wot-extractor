# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_results/presenters/packers/battle_info.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_results/presenters/packers/battle_info.py
from gui.battle_results.pbs_helpers.common import getArenaNameStr, getRegularFinishResultResource
from gui.battle_results.presenters.packers.interfaces import IBattleResultsPacker
from gui.battle_results.settings import BATTLE_RESULTS_RECORD as _RECORD

class BattleInfo(IBattleResultsPacker):

    @classmethod
    def packModel(cls, model, battleResults):
        reusable, results = battleResults.reusable, battleResults.results
        model.setArenaName(getArenaNameStr(reusable))
        common = results[_RECORD.COMMON]
        model.setBattleStartTime(common['arenaCreateTime'])
        model.setBattleDuration(common['duration'])
        cls._packTeamResult(model, reusable, results)

    @classmethod
    def _packTeamResult(cls, model, reusable, results):
        model.setWinStatus(cls._getWinStatus(reusable, results))
        model.setFinishReason(cls._getFinishReasonResource(reusable, results))

    @classmethod
    def _getFinishReasonResource(cls, reusable, results):
        return getRegularFinishResultResource(reusable.common.finishReason, reusable.getPersonalTeamResult())

    @classmethod
    def _getWinStatus(cls, reusable, results):
        return reusable.getPersonalTeamResult()
