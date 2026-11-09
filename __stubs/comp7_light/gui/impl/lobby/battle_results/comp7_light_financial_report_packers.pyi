# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/battle_results/comp7_light_financial_report_packers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.battle_results.presenters.packers.economics.currency_packers import CurrencyRecord as CurrencyRecord
from gui.battle_results.settings import CurrenciesConstants as CurrenciesConstants
from gui.impl.gen.view_models.views.lobby.battle_results.currency_records_item_model import CurrencyRecordsItemModel as CurrencyRecordsItemModel
from gui.impl.gen.view_models.views.lobby.battle_results.currency_value_model import ValueModifiers as ValueModifiers
from fairplay_violation_types import FairplayViolations as FairplayViolations
from gui.impl.gen import R as R
from gui.battle_results.presenters.packers.economics.financial_report_packers import CreditsStatisticsPacker as CreditsStatisticsPacker, XpDetailsPacker as XpDetailsPacker, FreeXpDetailsPacker as FreeXpDetailsPacker
from gui.battle_results.presenters.packers.economics import free_xp_records as free_xp_records, xp_records as xp_records, common_records as common_records, credits_records as credits_records
COMP7_LIGHT_DESERTER_VIOLATION: Any

class Comp7LightCreditsStatisticsPacker(CreditsStatisticsPacker):
    _EARNED: tuple

class Comp7LightXpDetailsPacker(XpDetailsPacker):
    _EARNED: tuple

class Comp7LightFreeXpDetailsPacker(FreeXpDetailsPacker):
    _EARNED: tuple

def getComp7LightDeserterViolation(_, __, battleResults):
    ...
