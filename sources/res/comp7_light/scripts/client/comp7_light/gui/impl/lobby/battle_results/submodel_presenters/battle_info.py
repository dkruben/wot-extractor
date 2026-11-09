# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/battle_results/submodel_presenters/battle_info.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/client/comp7_light/gui/impl/lobby/battle_results/submodel_presenters/battle_info.py
from __future__ import absolute_import
import typing
from comp7_light.gui.impl.gen.view_models.views.lobby.battle_results.comp7_light_battle_info_model import Comp7LightBattleInfoModel
from comp7_core.gui.battle_results.components.comp7_core_components import checkIfDeserter
from fairplay_violation_types import FairplayViolations
from gui.impl.lobby.battle_results.submodel_presenters.battle_info import BattleInfoSubPresenter
if typing.TYPE_CHECKING:
    from frameworks.wulf import ViewModel
    from gui.battle_results.stats_ctrl import BattleResults

class Comp7LightBattleInfoSubPresenter(BattleInfoSubPresenter):

    @classmethod
    def getViewModelType(cls):
        return Comp7LightBattleInfoModel

    def packBattleResults(self, battleResults):
        super(Comp7LightBattleInfoSubPresenter, self).packBattleResults(battleResults)
        reusable = battleResults.reusable
        winStatus = reusable.getPersonalTeamResult()
        with self.getViewModel().transaction() as model:
            model.setWinStatus(winStatus)
            model.setIsLeave(checkIfDeserter(reusable, FairplayViolations.COMP7_LIGHT_DESERTER))
