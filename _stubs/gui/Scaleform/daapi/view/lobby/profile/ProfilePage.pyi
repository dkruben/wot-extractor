# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/profile/ProfilePage.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
from gui.Scaleform.daapi import LobbySubView as LobbySubView
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.hof.hof_helpers import getHofTabCounter as getHofTabCounter, isHofButtonNew as isHofButtonNew, showDisabledDialog as showDisabledDialog
from gui.Scaleform.daapi.view.meta.ProfileMeta import ProfileMeta as ProfileMeta
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.Scaleform.genConsts.PROFILE_CONSTANTS import PROFILE_CONSTANTS as PROFILE_CONSTANTS
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.Scaleform.locale.PROFILE import PROFILE as PROFILE
from gui.collection.account_settings import getCollectionsTabCounter as getCollectionsTabCounter
from gui.limited_ui.lui_rules_storage import LUI_RULES as LUI_RULES
from gui.shared import events as events, g_eventBus as g_eventBus
from gui.shared.event_bus import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from helpers import dependency as dependency
from helpers.i18n import makeString as makeString
from skeletons.gui.game_control import IAchievements20Controller as IAchievements20Controller, ILimitedUIController as ILimitedUIController, ICollectionsSystemController as ICollectionsSystemController, IAchievementsController as IAchievementsController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from gui.Scaleform.daapi.view.lobby.profile.sound_constants import ACHIEVEMENTS_SOUND_SPACE as ACHIEVEMENTS_SOUND_SPACE
from gui.Scaleform.daapi.view.lobby.hof.web_handlers import createHofWebHandlers as createHofWebHandlers
from gui.Scaleform.daapi.view.lobby.hof.hof_helpers import getHofDisabledKeys as getHofDisabledKeys, onServerSettingsChange as onServerSettingsChange
from gui.shared.events import ProfilePageEvent as ProfilePageEvent, CollectionsEvent as CollectionsEvent
_LUI_RULES: tuple
_logger: Any

class ProfilePage(LobbySubView, ProfileMeta):
    lobbyContext: Any
    _limitedUIController: Any
    __achievements20Controller: Any
    __advAchmntCtrl: Any
    __collectionsSystem: Any
    _COMMON_SOUND_SPACE = ACHIEVEMENTS_SOUND_SPACE
    __ctx: Any
    __tabNavigator: Any
    def __init__(self, ctx=None):
        ...
    @property
    def tabId(self):
        ...
    def registerFlashComponent(self, component, alias, *args):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    def onCloseProfile(self):
        ...
    def updateSubView(self, ctx):
        ...
    def _populate(self):
        ...
    def _invalidate(self, *args, **kwargs):
        ...
    def _dispose(self):
        ...
    def __isLuiRuleProfileCompleted(self, *_):
        ...
    def __dossierUpdateCallBack(self, _):
        ...
    def __getSectionsData(self, resetSelectedAlias=False):
        ...
    @property
    def __isHofEnabled(self):
        ...
    def __onServerSettingChanged(self, diff):
        ...
    def __onCollectionsSettingsChanged(self):
        ...
    def __getTotalUnseenAdvancedAchievementsCount(self):
        ...
    def __updateTabCounters(self):
        ...
    def __loadHofUrl(self, url):
        ...
    def __onProfileVisited(self):
        ...
    def __onUnseenAchievementsUpdate(self):
        ...
    def __onCollectionTabUpdated(self, *_):
        ...
