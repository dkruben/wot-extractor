# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_core/scripts/client/comp7_core/gui/impl/lobby/tooltips/entry_point_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from comp7_core.gui.impl.lobby.comp7_core_helpers.comp7_core_model_helpers import setSeasonInfo as setSeasonInfo
from frameworks.wulf.view.array import fillIntsArray as fillIntsArray
from gui.impl.gen.view_models.views.lobby.user_missions.constants.event_banner_state import EventBannerState as EventBannerState
from gui.impl.pub import ViewImpl as ViewImpl
from helpers.time_utils import getServerUTCTime as getServerUTCTime
from math_common import round_py2_style_int as round_py2_style_int
_logger: Any

class Comp7CoreEntryPointTooltip(ViewImpl):
    _banner: Any
    def __init__(self, settings, eventBanner):
        ...
    @property
    def _modeController(self):
        ...
    @property
    def _seasonStateClazz(self):
        ...
    @property
    def _seasonNameClazz(self):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onStatusUpdated(self, _):
        ...
    def _onStatusTick(self):
        ...
    def _updateState(self):
        ...
    def __onPollServerTime(self):
        ...
