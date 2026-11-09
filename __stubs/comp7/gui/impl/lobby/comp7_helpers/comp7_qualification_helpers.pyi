# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/comp7_helpers/comp7_qualification_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from helpers import dependency as dependency
from comp7_common_const import BattleStatuses as BattleStatuses
from frameworks.wulf.view.array import fillViewModelsArray as fillViewModelsArray
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from comp7.gui.impl.gen.view_models.views.lobby.qualification_battle import BattleState as BattleState, QualificationBattle as QualificationBattle
from frameworks.wulf import Array as Array
from comp7.gui.impl.gen.view_models.views.lobby.qualification_model import QualificationModel as QualificationModel
BATTLE_STATES: dict

# decorador original: @dependency.replace_none_kwargs(...)
def setQualificationInfo(model, comp7Controller=None):
    ...
def setQualificationBattles(qualificationArray):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def __getQualificationBattleStates(comp7Controller=None):
    ...
def __createQualificationBattleModel(state):
    ...
