# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/tooltips/anomaly_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from halloween.configs.hw_upgrades_config import getConfig as getConfig
from halloween.gui.impl.gen.view_models.views.common.anomaly_model import AnomalyType as AnomalyType
from halloween.gui.impl.gen.view_models.views.lobby.tooltips.anomaly_tooltip_view_model import AnomalyTooltipViewModel as AnomalyTooltipViewModel
from halloween.skeletons.halloween_anomalies_controller import IHalloweenAnomaliesController as IHalloweenAnomaliesController
from helpers import dependency as dependency
from halloween.gui.game_control.halloween_anomalies_controller import AnomalyData as AnomalyData
from halloween.gui.impl.gen.view_models.views.common.anomaly_model import AnomalyState as AnomalyState
_ANOMALY_VEHICLE_KEY = 'vehicleAnomaly'

class AnomalyTooltipView(ViewImpl):
    __slots__: tuple
    _hwAnomaliesCtrl: Any
    __anomaly: Any
    __state: Any
    def __init__(self, anomaly, state):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self):
        ...
    def _getDescription(self, locR, anomalyName):
        ...
    def _getSpecialInfo(self, locR):
        ...
