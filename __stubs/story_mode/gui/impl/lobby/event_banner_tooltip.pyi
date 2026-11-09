# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/impl/lobby/event_banner_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf.view.view import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from helpers.time_utils import getTimestampFromUTC as getTimestampFromUTC, getServerUTCTime as getServerUTCTime
from story_mode.uilogging.story_mode.loggers import EventEntryPointTooltipLogger as EventEntryPointTooltipLogger
from story_mode_common.configs.story_mode_settings import settingsSchema as settingsSchema
from story_mode.gui.impl.gen.view_models.views.lobby.event_banner_tooltip_model import EventBannerTooltipModel as EventBannerTooltipModel

class EventBannerTooltip(ViewImpl):
    _uiLogger: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
