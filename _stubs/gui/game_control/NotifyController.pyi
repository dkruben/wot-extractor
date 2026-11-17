# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/NotifyController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from future.moves import pickle as pickle
import BigWorld as BigWorld
import Settings as Settings
from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from debug_utils import LOG_DEBUG as LOG_DEBUG, LOG_ERROR as LOG_ERROR
from frameworks.wulf import WindowLayer as WindowLayer
from gui.Scaleform.framework.managers.containers import POP_UP_CRITERIA as POP_UP_CRITERIA
from gui.app_loader import decorators as ap_decorators
from gui.shared import event_dispatcher as event_dispatcher
from gui.shared import events as events, g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.utils import graphics as graphics
from helpers import dependency as dependency
from py2to3.compat import base64compat as base64compat
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.game_control import INotifyController as INotifyController
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui import makeHtmlString as makeHtmlString
_Settings: Any

class NotifyController(INotifyController):
    LOW_FPS_VALUE = 20
    CURRENT_LOW_FPS_WARNING_VERSION = 1
    MIN_BATTLE_LENGHT = 180
    sessionProvider: Any
    settingsCore: Any
    __graphicsResetShown: Any
    __settings: Any
    def __init__(self):
        ...
    # decorador original: @ap_decorators.sf_lobby
    def app(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def updateBattleFpsInfo(self, avgBattleFps, battlePlayingTime):
        ...
    def _startUIListening(self):
        ...
    def _startPlayingTimeListening(self):
        ...
    def _stopUIListening(self):
        ...
    def _stopPlayingTimeListening(self):
        ...
    # decorador original: @adisp_process
    def __handleUiUpdated(self, _):
        ...
    def __handlePlayingTimeOnArena(self, event):
        ...
    # decorador original: @adisp_async
    def __showI18nDialog(self, key, callback, ctx=None):
        ...
    def __getSettingsWindow(self):
        ...
    def __closeSettingsWindow(self):
        ...
    def __updatePresetSetting(self, presetIdx=None):
        ...
    @classmethod
    def __getGraphicsPresetSetting(cls):
        ...
    def __downgradePresetIndex(self):
        ...
    def __isNeedToShowPresetChangingDialog(self):
        ...
    def __clearCurrentFpsInfo(self):
        ...
    def __updateLowFpsDialogVersion(self):
        ...
    def __readSettings(self):
        ...
    def __writeSettings(self):
        ...
    @classmethod
    def __wrapHtmlMessage(cls, message):
        ...
