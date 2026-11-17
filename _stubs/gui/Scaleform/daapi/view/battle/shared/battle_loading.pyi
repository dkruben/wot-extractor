# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/battle_loading.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BattleReplay as BattleReplay
from account_helpers.settings_core import settings_constants as settings_constants
from account_helpers.settings_core.options import BattleLoadingTipSetting as BattleLoadingTipSetting
from helpers import dependency as dependency
from helpers import tips as tips
from gui.battle_control.arena_info.interfaces import IArenaVehiclesController as IArenaVehiclesController
from gui.shared.formatters import text_styles as text_styles
from gui.Scaleform.daapi.view.meta.BaseBattleLoadingMeta import BaseBattleLoadingMeta as BaseBattleLoadingMeta
from ReplayEvents import g_replayEvents as g_replayEvents
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
_bBattleReplayLoadingShowed = False
DEFAULT_BATTLES_COUNT = 100

class BattleLoading(BaseBattleLoadingMeta, IArenaVehiclesController):
    sessionProvider: Any
    settingsCore: Any
    lobbyContext: Any
    gui: Any
    _battleCtx: Any
    _arenaVisitor: Any
    _isArenaTypeDataInited: Any
    def __init__(self, _=None):
        ...
    def startControl(self, battleCtx, arenaVisitor):
        ...
    def stopControl(self):
        ...
    def updateSpaceLoadProgress(self, progress):
        ...
    def invalidateArenaInfo(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _getBattlesCount(self):
        ...
    def _setTipsInfo(self):
        ...
    def _formatTipTitle(self, tipTitleText):
        ...
    def _formatTipBody(self, tipBody):
        ...
    def _addArenaTypeData(self):
        ...
    def _getSettingsID(self, loadingInfo, tip):
        ...
    def _makeVisualTipVO(self, arenaDP, tip=None):
        ...
    def _getViewSettingByID(self, settingID):
        ...

def _setBattleLoading(value):
    ...
def _onReplayTerminated(_):
    ...
def _isBattleLoadingShowed():
    ...
