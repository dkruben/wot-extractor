# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/dedication/dedication_reward_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.dedication.dedication_reward_view_model import DedicationRewardViewModel as DedicationRewardViewModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.server_events.bonuses import getNonQuestBonuses as getNonQuestBonuses
from gui.shared.missions.packers.bonus import packMissionsBonusModelAndTooltipData as packMissionsBonusModelAndTooltipData, getDefaultBonusPacker as getDefaultBonusPacker
from gui.sounds.filters import switchHangarOverlaySoundFilter as switchHangarOverlaySoundFilter

class DedicationRewardView(ViewImpl):
    __slots__: tuple
    __tooltipItems: Any
    __onCloseCallback: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTip(self, event):
        ...
    @staticmethod
    def _convertNonQuestBonuses(bonuses):
        ...
    def _initialize(self, bonuses, data, onClose):
        ...
    def _finalize(self):
        ...
    def _onLoading(self, bonuses, data, *args, **kwargs):
        ...
    def _setAwards(self, bonuses, data):
        ...

class DedicationRewardWindow(LobbyNotificationWindow):
    __slots__: tuple
    def __init__(self, bonuses, data, closeCallback):
        ...
