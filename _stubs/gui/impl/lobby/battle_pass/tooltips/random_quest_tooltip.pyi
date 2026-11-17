# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_pass/tooltips/random_quest_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.battle_pass.tooltips.random_quest_tooltip_model import RandomQuestTooltipModel as RandomQuestTooltipModel
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from shared_utils import first as first
from skeletons.gui.server_events import IEventsCache as IEventsCache
from gui.server_events.event_items import Quest as Quest

class RandomQuestTooltip(ViewImpl):
    __slots__: tuple
    __eventsCache: Any
    __quest: Any
    def __init__(self, requiredToken):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
