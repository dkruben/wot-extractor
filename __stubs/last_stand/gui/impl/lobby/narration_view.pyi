# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/narration_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import WWISE as WWISE
from gui.impl.gen import R as R
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from last_stand.gui.impl.gen.view_models.views.lobby.narration_view_model import NarrationViewModel as NarrationViewModel
from frameworks.wulf import WindowFlags as WindowFlags, WindowLayer as WindowLayer
from last_stand.gui.impl.lobby.base_view import SwitcherPresenter as SwitcherPresenter
from last_stand.gui.impl.lobby.widgets.parallax_view import ParallaxView as ParallaxView
from last_stand.gui.sounds import playSound as playSound, getSound2D as getSound2D
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from last_stand.gui.sounds.sound_constants import META_VOICEOVER_UNMUTE as META_VOICEOVER_UNMUTE, META_VOICEOVER_BUTTON_CLICK_UNMUTE as META_VOICEOVER_BUTTON_CLICK_UNMUTE, META_VOICEOVER_MUTE as META_VOICEOVER_MUTE, META_VOICEOVER_BUTTON_CLICK_MUTE as META_VOICEOVER_BUTTON_CLICK_MUTE, META_STORY_POINT_OPEN_SOUND as META_STORY_POINT_OPEN_SOUND, META_STORY_POINT_CLOSE_SOUND as META_STORY_POINT_CLOSE_SOUND
from last_stand.gui import ls_account_settings as ls_account_settings
from helpers import dependency as dependency
from last_stand.gui.ls_account_settings import AccountSettingsKeys as AccountSettingsKeys
from last_stand.skeletons.ls_story_point_controller import ILSStoryPointController as ILSStoryPointController
from last_stand.uilogging.last_stand.constants import NARRATION_PREFIX as NARRATION_PREFIX, START_MARKER_KEY as START_MARKER_KEY, END_MARKER_KEY as END_MARKER_KEY
from last_stand.uilogging.last_stand.loggers import NarrationEventLogger as NarrationEventLogger

# base nao representavel no stub: ViewComponent[...]
class NarrationView:
    lsStoryPointCtrl: Any
    LAYOUT_ID: Any
    __currentSlideIndex: Any
    _uiLogger: Any
    _sound: Any
    def __init__(self, layoutID=...):
        ...
    @property
    def viewModel(self):
        ...
    def _getChildComponents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def _onClose(self):
        ...
    def _playCurrentSlideSound(self):
        ...
    def _soundMarkerHandler(self, marker):
        ...
    def __onVoiceoverToggle(self):
        ...
    def __onSlide(self, args):
        ...
    def __prepareSelectedStoryPoint(self):
        ...
    def __updateButtonLock(self, tx):
        ...
    def __fillViewModel(self):
        ...
    def __onStoryPointStatusUpdated(self, token):
        ...

class NarrationWindow(LobbyNotificationWindow):
    __args: Any
    def __init__(self, layoutID, parent=None):
        ...
    def isParamsEqual(self, *args):
        ...
