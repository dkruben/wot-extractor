# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/battle/anomaly_recipes_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl import backport as backport
from gui.impl.auxiliary.tooltips.simple_tooltip import createSimpleTooltip as createSimpleTooltip
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from halloween.gui.halloween_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from halloween.gui.impl.common.anomalies_view_mixin import AnomaliesViewMixin as AnomaliesViewMixin
from halloween.gui.impl.gen.view_models.views.battle.anomaly_recipes_view_model import AnomalyRecipesViewModel as AnomalyRecipesViewModel
from halloween.gui.impl.gen.view_models.views.common.anomaly_model import AnomalyState as AnomalyState
from halloween.gui.scaleform.daapi.view.battle.anomalies_utils import selectAnomaly as selectAnomaly, getKnownAnomaliesIDs as getKnownAnomaliesIDs
from halloween.gui.sounds import playSound as playSound
from halloween.gui.sounds.sound_constants import AnomaliesSounds as AnomaliesSounds
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from typing import List as List
_logger: Any

class AnomalyRecipesView(AnomaliesViewMixin, ViewImpl):
    sessionProvider: Any
    _usedAnomalies: Any
    def __init__(self):
        ...
    def getAnomalyState(self, anomalyData):
        ...
    @property
    def knownAnomaliesIDs(self):
        ...
    @property
    def hwBattleGuiCtrl(self):
        ...
    @property
    def upgradeOptions(self):
        ...
    def createToolTip(self, event):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
    def __onChangeAnomaliesViewVisibility(self, isVisible):
        ...
    def __onAnomalyClick(self, args):
        ...
    def __onUpdateUsedAnomalies(self, usedAnomalies):
        ...
    def __onUpgradeOptionsUpdated(self, _):
        ...
