# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/lobby/epicBattleTraining/epic_battle_training_room.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frontline.gui.prb_control.entities.epic_battle_training.ctx import EpicTrainingSettingsCtx as EpicTrainingSettingsCtx
from adisp import adisp_process as adisp_process
from constants import PREBATTLE_TYPE as PREBATTLE_TYPE
from debug_utils import LOG_DEBUG as LOG_DEBUG
from gui import SystemMessages as SystemMessages
from gui.Scaleform.daapi.view.lobby.trainings import formatters as formatters
from gui.Scaleform.daapi.view.meta.EpicBattleTrainingRoomMeta import EpicBattleTrainingRoomMeta as EpicBattleTrainingRoomMeta
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.Scaleform.genConsts.MESSENGER_CHANNEL_CAROUSEL_ITEM_TYPES import MESSENGER_CHANNEL_CAROUSEL_ITEM_TYPES as MESSENGER_CHANNEL_CAROUSEL_ITEM_TYPES
from gui.Scaleform.genConsts.PREBATTLE_ALIASES import PREBATTLE_ALIASES as PREBATTLE_ALIASES
from gui.Scaleform.settings import ICONS_SIZES as ICONS_SIZES
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.prb_control.entities.base.legacy.ctx import GroupAssignLegacyCtx as GroupAssignLegacyCtx, GroupSwapInTeamLegacyCtx as GroupSwapInTeamLegacyCtx, GroupSwapBetweenTeamLegacyCtx as GroupSwapBetweenTeamLegacyCtx
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from gui.prb_control.items.prb_items import getPlayersSortKey as getPlayersSortKey
from gui.prb_control.settings import PREBATTLE_ROSTER as PREBATTLE_ROSTER, REQUEST_TYPE as REQUEST_TYPE
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, g_eventBus as g_eventBus
from gui.shared.events import ChannelCarouselEvent as ChannelCarouselEvent
from gui.shared.formatters import text_styles as text_styles
from helpers import int2roman as int2roman
from messenger.ext import channel_num_gen as channel_num_gen
from messenger.ext.channel_num_gen import SPECIAL_CLIENT_WINDOWS as SPECIAL_CLIENT_WINDOWS

class EpicBattleTrainingRoom(EpicBattleTrainingRoomMeta):
    _firstTime: Any
    def __init__(self, **kwargs):
        ...
    def showTrainingSettings(self):
        ...
    def onRostersChanged(self, entity, rosters, full):
        ...
    # decorador original: @adisp_process
    def onSwapTeamLane(self, fromTeam, fromLane, toTeam, toLane):
        ...
    # decorador original: @adisp_process
    def onChangeTeamLane(self, accID, team, lane):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _addListeners(self):
        ...
    def _removeListeners(self):
        ...
    def _handleSetPrebattleCoolDown(self, event):
        ...
    def _closeWindows(self):
        ...
    def _showRosters(self, entity, rosters):
        ...
    def _isObserverModeEnabled(self):
        ...
    def _updateTrainingRoom(self, event):
        ...
    def __makeAccountsDataForLane(self, accounts, lane, rLabel=None):
        ...
    def __updateWindowOpenState(self, flag):
        ...
