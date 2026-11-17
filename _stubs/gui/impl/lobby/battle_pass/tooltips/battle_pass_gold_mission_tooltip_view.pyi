# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_pass/tooltips/battle_pass_gold_mission_tooltip_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.battle_pass.tooltips.battle_pass_gold_mission_tooltip_view_model import BattlePassGoldMissionTooltipViewModel as BattlePassGoldMissionTooltipViewModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.money import Currency as Currency
from helpers import dependency as dependency
from shared_utils import first as first
from skeletons.gui.server_events import IEventsCache as IEventsCache

class BattlePassGoldMissionTooltipView(ViewImpl):
    __eventsCache: Any
    __token: Any
    def __init__(self, token):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
