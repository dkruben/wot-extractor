# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/collector20_reward/collector20_reward_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import DOSSIER_TYPE as DOSSIER_TYPE
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.common.awards_view_model import AwardsViewModel as AwardsViewModel
from gui.impl.lobby.collector20_reward.packers import getCollector20RewardsBonusPacker as getCollector20RewardsBonusPacker
from gui.impl.lobby.common.view_helpers import packBonusModelAndTooltipData as packBonusModelAndTooltipData
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.server_events.bonuses import DossierBonus as DossierBonus
import SoundGroups as SoundGroups
EXIT_EVENT = 'gui_hangar_award_screen_stop'

class Collector20RewardView(ViewImpl):
    __tooltipItems: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    def getTooltipData(self, event):
        ...
    def _onLoading(self, dossierRewards, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def __onClose(self, *_):
        ...

class Collector20RewardWindow(LobbyNotificationWindow):
    def __init__(self, dossierRewards, parent=None):
        ...
