# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/personal_missions_30/tooltips/missions_category_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.personal_missions_30.tooltips.missions_category_tooltip_model import MissionsCategoryTooltipModel as MissionsCategoryTooltipModel
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from skeletons.gui.server_events import IEventsCache as IEventsCache
from gui.server_events.event_items import PMOperation as PMOperation
from gui.impl.gen.view_models.views.lobby.personal_missions_30.common.enums import MissionCategory as MissionCategory

class MissionsCategoryTooltip(ViewImpl):
    __eventsCache: Any
    __category: Any
    __operation: Any
    def __init__(self, category, operation):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self):
        ...
