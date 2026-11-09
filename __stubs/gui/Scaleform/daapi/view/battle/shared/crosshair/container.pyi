# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/crosshair/container.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BattleReplay as BattleReplay
import GUI as GUI
import WWISE as WWISE
from PlayerEvents import g_playerEvents as g_playerEvents
from debug_utils import LOG_WARNING as LOG_WARNING, LOG_DEBUG as LOG_DEBUG, LOG_ERROR as LOG_ERROR
from gui import DEPTH_OF_Aim as DEPTH_OF_Aim
from gui.Scaleform.daapi.settings.views import BattleSharedLayoutType as BattleSharedLayoutType
from gui.Scaleform.daapi.view.battle.shared.crosshair import gm_factory as gm_factory, plugins as plugins, settings as settings
from gui.Scaleform.daapi.view.external_components import ExternalFlashComponent as ExternalFlashComponent
from gui.Scaleform.daapi.view.external_components import ExternalFlashSettings as ExternalFlashSettings
from gui.Scaleform.daapi.view.meta.CrosshairPanelContainerMeta import CrosshairPanelContainerMeta as CrosshairPanelContainerMeta
from gui.Scaleform.flash_wrapper import InputKeyMode as InputKeyMode
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES as BATTLE_VIEW_ALIASES
from gui.Scaleform.genConsts.AUTOLOADERBOOSTVIEWSOUNDS import AUTOLOADERBOOSTVIEWSOUNDS as AUTOLOADERBOOSTVIEWSOUNDS
from gui.Scaleform.locale.INGAME_GUI import INGAME_GUI as INGAME_GUI
from gui.Scaleform.daapi.view.battle.shared.hint_panel.plugins import RoleHelpPlugin as RoleHelpPlugin
from gui.app_loader import settings as app_settings
from gui.battle_control.battle_constants import CROSSHAIR_VIEW_ID as CROSSHAIR_VIEW_ID
from gui.impl import backport as backport
from gui.shared.events import GameEvent as GameEvent
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.utils.plugins import PluginsCollection as PluginsCollection
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from helpers import dependency as dependency, i18n as i18n, isPlayerAvatar as isPlayerAvatar
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from skeletons.gui.impl import IGuiLoader as IGuiLoader
_logger: Any
FADE_TIMEOUT = 7

class AutoloaderBoostSoundEvents(object):
    __slots__: tuple
    __EVENTS: dict
    @staticmethod
    def play(state):
        ...

class CrosshairPanelContainer(ExternalFlashComponent, CrosshairPanelContainerMeta):
    sessionProvider: Any
    guiLoader: Any
    EXTERNAL_FLASH_SETTINGS: Any
    __plugins: Any
    __gunMarkers: Any
    __viewID: Any
    __zoomFactor: Any
    __scale: Any
    __width: Any
    __height: Any
    __distance: Any
    __damage: Any
    __hasAmmo: Any
    __callbackDelayer: Any
    __isFaded: Any
    def __init__(self):
        ...
    def getPlugins(self):
        ...
    def getViewID(self):
        ...
    def setViewID(self, viewID):
        ...
    def setPosition(self, x, y):
        ...
    def setSize(self, width, height):
        ...
    def getScale(self):
        ...
    def setScale(self, scale):
        ...
    def getZoom(self):
        ...
    def setZoom(self, zoomFactor):
        ...
    def getDistance(self):
        ...
    def setDistance(self, distance):
        ...
    def clearDistance(self, immediate=True):
        ...
    def setMutableDamage(self, damage):
        ...
    def clearMutableDamage(self, immediate=True):
        ...
    def setHasAmmo(self, hasAmmo):
        ...
    def setSettings(self, vo):
        ...
    def createGunMarkers(self, markersInfo, vehicleInfo):
        ...
    def invalidateGunMarkers(self, markersInfo, vehicleInfo):
        ...
    def setGunMarkerColor(self, markerType, color):
        ...
    def startPlugins(self):
        ...
    def stopPlugins(self):
        ...
    def createExternalComponent(self):
        ...
    def as_playSound(self, value):
        ...
    def _populate(self):
        ...
    def _setSharedLayout(self):
        ...
    def _dispose(self):
        ...
    def _getPlugins(self):
        ...
    def _addPlugins(self, plugin):
        ...
    def __handleRoleHintToggled(self, event):
        ...
    def __toggleFade(self, isFaded):
        ...
    def __exceptionalFadeIn(self):
        ...
    def __configure(self):
        ...
    def __setGunMarkers(self, gunMarkers):
        ...
    def __clearGunMarkers(self):
        ...
