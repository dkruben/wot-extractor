# wot-extractor: STUB (.pyi) gerado a partir de sources/res/resource_well/scripts/client/resource_well/gui/impl/lobby/feature/tooltips/event_banner_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.user_missions.constants.event_banner_state import EventBannerState as EventBannerState
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from helpers import dependency as dependency, time_utils as time_utils
from resource_well.gui.impl.gen.view_models.views.lobby.tooltips.event_banner_tooltip_model import EventBannerTooltipModel as EventBannerTooltipModel
from resource_well.gui.impl.gen.view_models.views.lobby.tooltips.reward_info_model import RewardInfoModel as RewardInfoModel
from skeletons.gui.resource_well import IResourceWellController as IResourceWellController

class EventBannerTooltip(ViewImpl):
    __resourceWell: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __fillEventTime(self, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __fillRewards(self, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __fillEventState(self, model=None):
        ...
    def __onEventUpdated(self):
        ...
    def __onSettingsChanged(self):
        ...
