# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/quest_progress_top_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers.settings_core.options import QuestsProgressViewType as QuestsProgressViewType, QuestsProgressDisplayType as QuestsProgressDisplayType
from account_helpers.settings_core.settings_constants import QUESTS_PROGRESS as QUESTS_PROGRESS
from gui.Scaleform.daapi.view.meta.QuestProgressTopViewMeta import QuestProgressTopViewMeta as QuestProgressTopViewMeta
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
import SoundGroups as SoundGroups
from gui.battle_control import avatar_getter as avatar_getter
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext

class QuestProgressTopView(QuestProgressTopViewMeta):
    settingsCore: Any
    sessionProvider: Any
    lobbyContext: Any
    __isProgressAvailable: Any
    __isProgressEnabled: Any
    __isFlagVisible: Any
    __isVisibleForCurrentVehicle: Any
    __isPMBattleProgressEnabled: Any
    def __init__(self):
        ...
    def onPlaySound(self, soundType):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __onSettingsChange(self, diff):
        ...
    def __onFullConditionsUpdate(self, *args):
        ...
    def __onVehicleControlling(self, vehicle):
        ...
    def __setVisibility(self):
        ...
    def __onShowAnimation(self, *args):
        ...
