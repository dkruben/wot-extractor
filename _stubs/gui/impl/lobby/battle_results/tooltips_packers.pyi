# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_results/tooltips_packers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import inspect as inspect
from gui.battle_results.presenters.packers.tooltips.efficiency_tooltips import DamageAssistedParameter as DamageAssistedParameter, SpottedParameter as SpottedParameter, DamageBlockedByArmorParameter as DamageBlockedByArmorParameter, DamageDealtParameter as DamageDealtParameter, KillsParameter as KillsParameter, StunParameter as StunParameter, CapturePointsParameter as CapturePointsParameter, DefencePointsParameter as DefencePointsParameter, EfficiencyTooltipsPacker as EfficiencyTooltipsPacker
from gui.impl.gen.view_models.views.lobby.battle_results.base_capture_info_model import BaseCaptureInfoModel as BaseCaptureInfoModel
from gui.impl.gen.view_models.views.lobby.battle_results.detailed_personal_efficiency_item_model import DetailedPersonalEfficiencyItemModel as DetailedPersonalEfficiencyItemModel
DETAILED_PARAMETERS_TO_TOOLTIP_MAP: dict

class BattleEfficiencyTooltipsPacker(EfficiencyTooltipsPacker):
    _TOOLTIPS = DETAILED_PARAMETERS_TO_TOOLTIP_MAP
    @staticmethod
    def _getEfficiencyParameter(paramType):
        ...
