# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/pet_system/event_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BigWorld as BigWorld
from frameworks.wulf import WindowFlags as WindowFlags, WindowStatus as WindowStatus
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.pet_system.event_view_model import EventViewModel as EventViewModel
from gui.impl.lobby.common.view_helpers import packBonusModelAndTooltipData as packBonusModelAndTooltipData
from gui.impl.pub import WindowImpl as WindowImpl
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.server_events.bonuses import getNonQuestBonuses as getNonQuestBonuses, CreditsBonus as CreditsBonus, GoodiesBonus as GoodiesBonus, ItemsBonus as ItemsBonus
from gui.shared.missions.packers.bonus import getDefaultBonusPacker as getDefaultBonusPacker
from helpers import dependency as dependency
from messenger.m_constants import SCH_CLIENT_MSG_TYPE as SCH_CLIENT_MSG_TYPE
from pet_system_common import pet_constants as pet_constants
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.pet_system import IPetSystemController as IPetSystemController
from skeletons.gui.system_messages import ISystemMessages as ISystemMessages
from typing import List as List
from gui.server_events.bonuses import SimpleBonus as SimpleBonus

class PetEvent(ViewComponent):
    LAYOUT_ID: Any
    __petController: Any
    __lobbyContext: Any
    __systemMessages: Any
    _ctx: Any
    __packer: Any
    __tooltipData: Any
    def __init__(self, viewModel, ctx):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def createToolTip(self, event):
        ...
    def getTooltipData(self, event):
        ...
    def _updateData(self):
        ...
    def _updateRewards(self):
        ...
    @staticmethod
    def __getRewards(rewardsData):
        ...
    def _onServerSettingsChanged(self, diff):
        ...
    def _onClose(self):
        ...
    def _pushRewardNotification(self, rewards):
        ...
    def __pushCreditsNotification(self, item):
        ...
    def __pushGoodieNotification(self, item):
        ...
    def __pushItemNotification(self, item):
        ...

class EventView(PetEvent):
    LAYOUT_ID: Any
    def __init__(self, ctx):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...

class EventViewWindow(WindowImpl):
    def __init__(self, layer, **kwargs):
        ...
    def show(self, focus=True):
        ...
    def _onFocus(self, focused):
        ...
