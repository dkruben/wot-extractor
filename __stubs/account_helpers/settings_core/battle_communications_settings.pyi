# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/account_helpers/settings_core/battle_communications_settings.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BattleReplay as BattleReplay
from Event import Event as Event
from PlayerEvents import g_playerEvents as g_playerEvents
from account_helpers.settings_core.settings_constants import BattleCommStorageKeys as BattleCommStorageKeys
from helpers import dependency as dependency
from pve_battle_hud import WidgetType as WidgetType
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore, ISettingsCache as ISettingsCache, IBattleCommunicationsSettings as IBattleCommunicationsSettings
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.battle_control.controllers.vse_hud_settings_ctrl.settings.battle_communication import BattleCommunicationModel as BattleCommunicationModel

class BattleCommunicationSettings(IBattleCommunicationsSettings):
    __slots__: tuple
    _settingsCore: Any
    _settingsCache: Any
    _sessionProvider: Any
    onChanged: Any
    _isEnabled: Any
    _showStickyMarkers: Any
    _showInPlayerList: Any
    _showCalloutMessages: Any
    _showLocationMarkers: Any
    _showBaseMarkers: Any
    _enableCommendationsFeedback: Any
    def __init__(self):
        ...
    @property
    def isEnabled(self):
        ...
    @property
    def showStickyMarkers(self):
        ...
    @property
    def showInPlayerList(self):
        ...
    @property
    def showCalloutMessages(self):
        ...
    @property
    def showLocationMarkers(self):
        ...
    @property
    def showBaseMarkers(self):
        ...
    @property
    def showCommendationsFeedbackOnReceive(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def _quitBattleHandler(self):
        ...
    def _avatarBecomePlayerHandler(self):
        ...
    def _onSettingsReady(self):
        ...
    def _coreSettingsChangeHandler(self, _):
        ...
    def _vseSettingsChangeHandler(self, settingsID):
        ...
    def _coreEnabled(self, name):
        ...
    def _resolveEnabled(self):
        ...
