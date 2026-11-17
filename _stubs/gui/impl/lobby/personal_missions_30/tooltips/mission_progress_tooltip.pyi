# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/personal_missions_30/tooltips/mission_progress_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks.wulf import ViewSettings as ViewSettings
from frameworks.wulf.view.array import fillStringsArray as fillStringsArray
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.personal_missions_30.tooltips.mission_progress_tooltip_model import MissionProgressTooltipModel as MissionProgressTooltipModel
from gui.impl.lobby.personal_missions_30.views_helpers import getMissionConfigData as getMissionConfigData
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.impl.lobby.personal_missions_30.views_helpers import ConditionsConfig as ConditionsConfig
from gui.server_events.event_items import PersonalMission as PersonalMission

class MissionProgressTooltip(ViewImpl):
    __itemsCache: Any
    __mission: Any
    __isCompleted: Any
    def __init__(self, mission, isCompleted):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self):
        ...
