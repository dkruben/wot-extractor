# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/presenters/packers/personal_efficiency.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.battle_results.presenters.packers.interfaces import IBattleResultsPacker as IBattleResultsPacker
from gui.battle_results.settings import BATTLE_RESULTS_RECORD as _RECORD
from gui.impl.gen.view_models.views.lobby.battle_results.detailed_personal_efficiency_item_model import DetailedPersonalEfficiencyItemModel as DetailedPersonalEfficiencyItemModel
from gui.impl.gen.view_models.views.lobby.battle_results.personal_efficiency_model import PersonalEfficiencyModel as PersonalEfficiencyModel, ValueType as ValueType
EFFICIENCY_ITEMS_TO_PROPERTIES: dict

class PersonalEfficiency(IBattleResultsPacker):
    _PARAMETERS: dict
    _DEFAULT_PARAMS: tuple
    _VALUE_EXTRACTORS: dict
    _VALUE_TYPES: dict
    _EFFICIENCY_ITEM_MODEL_CLS = PersonalEfficiencyModel
    @classmethod
    def packModel(cls, model, battleResults):
        ...
    @classmethod
    def _createParameterModel(cls, parameter, vehicleInfo):
        ...
    @classmethod
    def _getParameterList(cls, vehicle, _):
        ...
