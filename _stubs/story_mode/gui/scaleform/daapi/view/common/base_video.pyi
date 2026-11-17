# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/common/base_video.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from logging import getLogger as getLogger
import BigWorld as BigWorld
import SoundGroups as SoundGroups
import typing as typing
import WWISE as WWISE
import Windowing as Windowing
from PlayerEvents import g_playerEvents as g_playerEvents
from account_helpers import AccountSettings as AccountSettings
from account_helpers.settings_core.settings_constants import SOUND as SOUND
from gui import g_keyEventHandlers as g_keyEventHandlers
from gui.impl import backport as backport
from gui.impl.gen import R as R
from helpers import i18n as i18n, dependency as dependency
from story_mode.gui.scaleform.daapi.view.meta.IntroVideoMeta import IntroVideoMeta as IntroVideoMeta
from story_mode.skeletons.story_mode_controller import IStoryModeController as IStoryModeController
from story_mode.uilogging.story_mode.consts import LogButtons as LogButtons
from story_mode_common.story_mode_constants import LOGGER_NAME as LOGGER_NAME
from story_mode.gui.scaleform.daapi.view.model.video_settings_model import VideoSettingsModel as VideoSettingsModel
from story_mode.uilogging.story_mode.loggers import BaseVideoLogger as BaseVideoLogger
_logger: Any

class BaseVideo(IntroVideoMeta):
    _storyModeCtrl: Any
    _uiLogger: Any
    _isVideoStarted: Any
    _missionId: Any
    _videoSettings: Any
    def __init__(self, ctx):
        ...
    def onVideoStarted(self):
        ...
    def onVideoComplete(self):
        ...
    def onSkipButtonVisible(self):
        ...
    def onSkipButtonClicked(self):
        ...
    def _getSettings(self):
        ...
    def _getLogger(self):
        ...
    def _getLoadingImage(self):
        ...
    @property
    def _canVideoBePaused(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _closeWindow(self):
        ...
    def _onWindowAccessibilityChanged(self, isAccessible):
        ...
    def _soundMarkerHandler(self, marker):
        ...
    def _handleKeyEvent(self, event):
        ...
    def _disconnectHandler(self):
        ...

def sendWWISEEventGlobal(event):
    ...
