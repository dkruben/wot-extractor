# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/anomalies_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import WindowFlags as WindowFlags
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.impl.gen import R as R
from gui.impl.pub import WindowImpl as WindowImpl
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from halloween.gui.impl.common.anomalies_view_mixin import AnomaliesViewMixin as AnomaliesViewMixin
from halloween.gui.impl.gen.view_models.views.common.anomaly_model import AnomalyState as AState
from halloween.gui.impl.gen.view_models.views.lobby.anomalies_view_model import AnomaliesViewModel as AnomaliesViewModel
from halloween.gui.impl.lobby.hw_helpers.anomalies_helpers import getKnownAnomaliesIDs as getKnownAnomaliesIDs, setAnomalyAsShowed as setAnomalyAsShowed, getShowedAnomaliesIDs as getShowedAnomaliesIDs
from halloween.gui.impl.lobby.tooltips.anomaly_tooltip import AnomalyTooltipView as AnomalyTooltipView
from halloween.gui.sounds import playSound as playSound
from halloween.gui.sounds.sound_constants import AnomaliesSounds as AnomaliesSounds
from halloween.skeletons.halloween_anomalies_controller import IHalloweenAnomaliesController as IHalloweenAnomaliesController
from halloween.uilogging.loggers import HWMetricsLogger as HWMetricsLogger
from halloween.uilogging.logging_constants import HWLogKeys as HWLogKeys, HWLogActions as HWLogActions
from helpers import dependency as dependency

class AnomaliesView(AnomaliesViewMixin, ViewComponent):
    _MAX_SKIN_ID: Any
    _hwAnomaliesCtrl: Any
    __uiLogger: Any
    def __init__(self):
        ...
    def getAnomalyState(self, anomalyData):
        ...
    @property
    def knownAnomaliesIDs(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __onClose(self):
        ...
    def __onAnomalyAcknowledged(self, args):
        ...
    def __onRefreshData(self):
        ...

class AnomaliesWindow(WindowImpl):
    def __init__(self, layer, **_):
        ...
