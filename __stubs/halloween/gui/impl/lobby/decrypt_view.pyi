# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/decrypt_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.impl.backport import createTooltipData as createTooltipData, BackportTooltipWindow as BackportTooltipWindow
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.shared import g_eventBus as g_eventBus, events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from halloween.gui import halloween_account_settings as halloween_account_settings
from halloween.gui.halloween_account_settings import AccountSettingsKeys as AccountSettingsKeys
from halloween.gui.impl.gen.view_models.views.lobby.decrypt_view_model import DecryptViewModel as DecryptViewModel
from halloween.gui.impl.lobby.hw_helpers import fillRewards as fillRewards
from halloween.gui.impl.lobby.tooltips.vehicle_tooltip import VehicleTooltipView as VehicleTooltipView
from halloween.gui.shared.event_dispatcher import showOutroVideo as showOutroVideo, showDecryptWindowView as showDecryptWindowView
from halloween.gui.shared.events import HWHangarEvent as HWHangarEvent
from halloween.gui.sounds import playSound as playSound
from halloween.gui.sounds.sound_constants import META_QUANTUM_VO_ON as META_QUANTUM_VO_ON, META_QUANTUM_VO_OFF as META_QUANTUM_VO_OFF, META_QUANTUM_SCREEN_ENTER as META_QUANTUM_SCREEN_ENTER, META_QUANTUM_SCREEN_EXIT as META_QUANTUM_SCREEN_EXIT
from halloween.skeletons.halloween_artefacts_controller import IHalloweenArtefactsController as IHalloweenArtefactsController
from halloween.skeletons.halloween_bestiary_controller import IHalloweenBestiaryController as IHalloweenBestiaryController
from halloween.skeletons.halloween_controller import IHalloweenController as IHalloweenController
from halloween.uilogging.loggers import DecryptionMetricsLogger as DecryptionMetricsLogger
from halloween.uilogging.logging_constants import HWLogKeys as HWLogKeys
from helpers import dependency as dependency
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from halloween_common.halloween_constants import HWStoryChoiceSettings as HWStoryChoiceSettings
from halloween.gui.game_control.halloween_artefacts_controller import Artefact as Artefact
_R_BACKPORT_TOOLTIP: Any
_SOUND_TAG = 'sound'

class DecryptView(ViewImpl):
    _hwArtefactsCtrl: Any
    _hwBestiaryCtrl: Any
    _hwController: Any
    _MAX_BONUSES_IN_VIEW = 5
    __artefactID: Any
    __isOutroDisabled: Any
    __isLastArtefactDisabled: Any
    __isRewardScreen: Any
    __bonusCache: Any
    __idGen: Any
    __decryptUILogger: Any
    def __init__(self, artefactID, isRewardScreen=False, disableOutro=False, disableLastArtefact=False):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def isMuted(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onShown(self):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def __onClose(self):
        ...
    def __onOutroVideo(self):
        ...
    def __onMuted(self):
        ...
    def __onChangeQuest(self, args):
        ...
    def __isPreviousArtefactAvailable(self, artefactIndex):
        ...
    def __isNextArtefactAvailable(self, artefactIndex):
        ...
    def __fillViewModel(self):
        ...
    def _isArtefactSoundEnabled(self):
        ...

class DecryptWindow(LobbyNotificationWindow):
    _args: Any
    def __init__(self, artefactID, isRewardScreen=None, disableOutro=False, disableLastArtefact=False, parent=None):
        ...
    def isParamsEqual(self, *args):
        ...
