# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/battle_results/submodel_presenters/battle_info.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from comp7_light.gui.impl.gen.view_models.views.lobby.battle_results.comp7_light_battle_info_model import Comp7LightBattleInfoModel as Comp7LightBattleInfoModel
from comp7_core.gui.battle_results.components.comp7_core_components import checkIfDeserter as checkIfDeserter
from fairplay_violation_types import FairplayViolations as FairplayViolations
from gui.impl.lobby.battle_results.submodel_presenters.battle_info import BattleInfoSubPresenter as BattleInfoSubPresenter
from frameworks.wulf import ViewModel as ViewModel
from gui.battle_results.stats_ctrl import BattleResults as BattleResults

class Comp7LightBattleInfoSubPresenter(BattleInfoSubPresenter):
    @classmethod
    def getViewModelType(cls):
        ...
    def packBattleResults(self, battleResults):
        ...
