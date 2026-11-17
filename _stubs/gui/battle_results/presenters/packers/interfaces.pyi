# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/presenters/packers/interfaces.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks.wulf import ViewModel as ViewModel, Array as Array
from gui.battle_results.stats_ctrl import BattleResults as BattleResults
from gui.battle_results.reusable.shared import VehicleSummarizeInfo as VehicleSummarizeInfo
from gui.impl.gen.view_models.views.lobby.battle_results.simple_stats_parameter_model import SimpleStatsParameterModel as SimpleStatsParameterModel
BattleResultsComponentModelType: Any
TooltipModelType: Any

class IBattleResultsPacker(object):
    @classmethod
    def packModel(cls, model, battleResults):
        ...
    @classmethod
    def updateModel(cls, model, battleResults, ctx=None, isFullUpdate=True):
        ...

class ICurrencyPacker(object):
    @classmethod
    def packModel(cls, model, currencyType, battleResults):
        ...

class IStatisticsPacker(object):
    @classmethod
    def packModel(cls, model, info, battleResult):
        ...

class ITooltipPacker(object):
    @classmethod
    def packTooltip(cls, model, battleResults, ctx=None):
        ...
