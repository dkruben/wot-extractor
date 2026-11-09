# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/king_reward_congrats_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import WWISE as WWISE
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow, createTooltipData as createTooltipData
from gui.impl.gen import R as R
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.shared.event_dispatcher import showVehicleHubOverview as showVehicleHubOverview
from halloween.gui.shared.event_dispatcher import showBestiaryWindow as showBestiaryWindow
from halloween.gui.impl.gen.view_models.views.lobby.king_reward_congrats_view_model import KingRewardCongratsViewModel as KingRewardCongratsViewModel
from halloween.gui.impl.lobby.hw_helpers import fillRewards as fillRewards, fillGiftVehicleModel as fillGiftVehicleModel, getEnemyByArtefactID as getEnemyByArtefactID
from halloween.gui.impl.lobby.base_view import BaseView as BaseView
from halloween.gui.sounds import playSound as playSound
from halloween.gui.sounds.sound_constants import KING_REWARD_WINDOW_ENTER as KING_REWARD_WINDOW_ENTER, KING_REWARD_WINDOW_EXIT as KING_REWARD_WINDOW_EXIT, KingRewardState as KingRewardState
from halloween.skeletons.halloween_artefacts_controller import IHalloweenArtefactsController as IHalloweenArtefactsController
from halloween.skeletons.halloween_bestiary_controller import IHalloweenBestiaryController as IHalloweenBestiaryController
from helpers import dependency as dependency
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from halloween_common.halloween_constants import HWStoryChoiceSettings as HWStoryChoiceSettings
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from halloween.gui.game_control.halloween_bestiary_controller import EnemyData as EnemyData
_R_BACKPORT_TOOLTIP: Any

class KingRewardCongratsView(BaseView):
    layoutID: Any
    _MAX_BONUSES_IN_VIEW = 5
    _guiLoader: Any
    _hwArtefactsCtrl: Any
    _hwBestiaryCtrl: Any
    __artefactID: Any
    __idGen: Any
    __bonusCache: Any
    def __init__(self, layoutID, artefactID):
        ...
    def createToolTip(self, event):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
    def _onClose(self):
        ...
    def _onToOutro(self):
        ...
    def _onToGarage(self):
        ...
    def __fillGiftVehicle(self):
        ...
    def __fillRewards(self):
        ...

class KingRewardCongratsWindow(LobbyNotificationWindow):
    _args: Any
    def __init__(self, layoutID, artefactID, parent=None):
        ...
    def isParamsEqual(self, *args):
        ...
