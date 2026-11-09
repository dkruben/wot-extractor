# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/battle_results/tooltips/total_efficiency_tooltips.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.battle_results.presenters.packers.tooltips.efficiency_tooltips import KillsParameter as KillsParameter, StunParameter as StunParameter, SpottedParameter as SpottedParameter, DefencePointsParameter as DefencePointsParameter, DamageDealtParameter as DamageDealtParameter, DamageAssistedParameter as DamageAssistedParameter, DamageBlockedByArmorParameter as DamageBlockedByArmorParameter, CapturePointsParameter as CapturePointsParameter, EfficiencyTooltipsPacker as EfficiencyTooltipsPacker
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.battle_results.efficiency_param_constants import EfficiencyParamConstants as EfficiencyParamConstants
from soft_exception import SoftException as SoftException
from gui.battle_results.stats_ctrl import BattleResults as BattleResults
from gui.impl.gen.view_models.views.lobby.battle_results.tooltips.efficiency_tooltip_model import EfficiencyTooltipModel as EfficiencyTooltipModel
_STR_PATH = R.strings.fun_battle_results.efficiencyTooltip.header
_FUN_PARAMETERS_TO_TOOLTIP_MAP: dict

class FunTotalKillsParameter(KillsParameter):
    _TITLE = _STR_PATH.kills

class FunTotalDamageDealtParameter(DamageDealtParameter):
    _TITLE = _STR_PATH.damageDealt

class FunTotalStunParameter(StunParameter):
    _TITLE = _STR_PATH.damageAssistedStun

class FunTotalDamageBlockedByArmorParameter(DamageBlockedByArmorParameter):
    _TITLE = _STR_PATH.damageBlockedByArmor

class FunTotalDamageAssistedParameter(DamageAssistedParameter):
    _TITLE = _STR_PATH.damageAssisted

class FunTotalSpottedParameter(SpottedParameter):
    _TITLE = _STR_PATH.spotted

class FunTotalCapturePointsParameter(CapturePointsParameter):
    _TITLE = _STR_PATH.capturePoints

class FunTotalDefencePointsParameter(DefencePointsParameter):
    _TITLE = _STR_PATH.droppedCapturePoints

class FunEfficiencyTooltipsPacker(EfficiencyTooltipsPacker):
    _TOOLTIPS = _FUN_PARAMETERS_TO_TOOLTIP_MAP
    @classmethod
    def packTooltip(cls, model, battleResults, ctx=None):
        ...
