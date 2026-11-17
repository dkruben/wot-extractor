# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/clan_supply/rewards_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import SoundGroups as SoundGroups
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.impl import backport as backport
from gui.impl.auxiliary.tooltips.compensation_tooltip import VehicleCompensationTooltipContent as VehicleCompensationTooltipContent
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.clan_supply.rewards_view_model import RewardsViewModel as RewardsViewModel, RewardingType as RewardingType
from gui.impl.gen.view_models.views.loot_box_compensation_tooltip_types import LootBoxCompensationTooltipTypes as LootBoxCompensationTooltipTypes
from gui.impl.gen.view_models.views.loot_box_vehicle_compensation_tooltip_model import LootBoxVehicleCompensationTooltipModel as LootBoxVehicleCompensationTooltipModel
from gui.impl.lobby.clan_supply.bonus_packers import composeBonuses as composeBonuses, findVehicle as findVehicle, getClanSupplyBonusPacker as getClanSupplyBonusPacker, BONUSES_ORDER as BONUSES_ORDER
from gui.impl.lobby.common.view_helpers import packBonusModelAndTooltipData as packBonusModelAndTooltipData
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.shared.event_dispatcher import selectVehicleInHangar as selectVehicleInHangar
from gui.impl.backport import TooltipData as TooltipData
from gui.server_events.bonuses import SimpleBonus as SimpleBonus

class RewardsView(ViewImpl):
    __slots__: tuple
    __tooltips: Any
    __vehicleCD: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def getTooltipData(self, event):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, isElite, rewards, *args, **kwargs):
        ...
    def __onClose(self):
        ...
    def __onGoToHangar(self):
        ...
    @staticmethod
    def __mainVehicleBonusAllocator(bonuses):
        ...

class RewardsViewWindow(LobbyNotificationWindow):
    __slots__: tuple
    def __init__(self, isElite, rewards, parent=None):
        ...
